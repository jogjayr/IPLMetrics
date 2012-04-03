## Contains utility classes.
from bs4 import BeautifulSoup
from datetime import date
import urllib, re, calendar

class ProfileScraper:
	
	def __init__(self, profile_id):
		self.profile_id = profile_id
		profile_url = "http://www.espncricinfo.com/ci/content/player/" + self.profile_id + ".html"
		response = urllib.urlopen(profile_url)
		self.soup = BeautifulSoup(response.read())

	def scrape_profile(self):
		profile = {}
		profile["player_info"] = self.scrape_player_info()
		profile["batting_stats"] = self.scrape_batting_stats()
		return profile

	def scrape_player_info(self):
		player_info = {}
		month_dict = dict((v,k) for k,v in enumerate(calendar.month_name))
		player_full_name = self.soup.find("p", "ciPlayerinformationtxt").find("span").getText()
		player_name_array = re.split(" ", player_full_name)
		length = len(player_name_array)
		player_info["FirstName"] = player_name_array[0]
		player_info["LastName"] = player_name_array[length - 1]
		player_info["MiddleName"] = ""
		dob_array = re.split(" |,", self.soup.find_all("p", "ciPlayerinformationtxt")[1].getText())
		dob_array = dob_array[1:5]

		dob = date(int(dob_array[3]), month_dict[dob_array[0].strip()], int(dob_array[1]))
		for i in range(1, length - 1):
			player_info["MiddleName"] = player_info["MiddleName"] + player_name_array[i] + " "

		player_info["DateOfBirth"] = dob
		return player_info

	def scrape_batting_stats(self):

		batting_stats_soup = self.soup.find_all("table", "engineTable", limit=1)
		batting_stats_soup = batting_stats_soup[0].find_all("tr", "data1")
		batting_stats = []
		batting_stat_instance = {}
		batting_metrics = ["Type", "Matches", "Innings", "NotOuts", "Runs", "HighScore", "Average", "BallsFaced", "StrikeRate", "Centuries", "Fifties", "Fours", "Sixes", "Catches", "Stumpings"]
		for tag in batting_stats_soup:
			batting_stats_row = tag.find_all("td")
			# batting_stats_key = batting_stats_row[0].getText()
			for index in range(len(batting_stats_row)):
				batting_stat_instance[batting_metrics[index]] = batting_stats_row[index].getText()

			batting_stats.append(batting_stat_instance)
			batting_stat_instance = {}


		return batting_stats
