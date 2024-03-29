## Contains utility classes.
from bs4 import BeautifulSoup
from datetime import date
import urllib, re, calendar, json





class SquadScraper:
	pipes_lookup = {
		"CSK": "http://pipes.yahoo.com/pipes/pipe.run?_id=cba6df8913eab238ead7377fef7e2b5a&_render=json",
		"DC" : "http://pipes.yahoo.com/pipes/pipe.run?_id=56325f18c0dc8bf9c7cdf167f555912a&_render=json",
		"DD" : "http://pipes.yahoo.com/pipes/pipe.run?_id=ce40eddcd1bc236c290e13effeb9e512&_render=json",
		"KXP": "http://pipes.yahoo.com/pipes/pipe.run?_id=d5eae8ddc8449eba91a9ac5e67d6b551&_render=json"
	}


	def scrape_entire_squad(self, team_name):
		url = self.pipes_lookup[team_name]
		response_obj = json.load(urllib.urlopen(url))
		markup_list = response_obj["value"]["items"]
		returnVal = []
		for item in markup_list:
			tag = BeautifulSoup(item["content"]).find("a")
			if(tag != None):
				id_finder = re.findall("\d*.html", tag["href"])
				if len(id_finder) == 1:
					returnVal.append(id_finder[0].split(".")[0])

		return returnVal



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

		# Lookup dict for month number, given full month name
		month_dict = dict((v,k) for k,v in enumerate(calendar.month_name))
		player_info["Country"] = self.soup.find_all("h1", "SubnavSitesection")[0].get_text().split("/\n")[1].strip()
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
			
			for index in range(len(batting_stats_row)):

				stat_item = batting_stats_row[index].getText()
				# stat_item = re.sub("\D", "", stat_item)
				if(index != 0 and index != 6 and index != 8):
					stat_item = re.sub("\D", "", stat_item)
					
				if stat_item == "" or stat_item == "-":
					stat_item = -1

				batting_stat_instance[batting_metrics[index]] = stat_item


			batting_stats.append(batting_stat_instance)
			batting_stat_instance = {}


		return batting_stats


class InningsScraper:		

	class_lookup = {
		"Test" : "1",
		"ODI" : "2",
		"T20I" : "3",
		"WTest": "8", #W prefix indicates women's
		"WODI": "9",
		"WT20I": "10",
		"CombinedTestODIT20I": "11",
		"U19Tests": 20,
		"U19ODI": 21,
	}

	def __init__(self, profile_id):
		self.url = "http://stats.espncricinfo.com/ci/engine/player/" + profile_id + ".html?class=1;template=results;type=batting;view=innings"
		response = urllib.urlopen(profile_url)
		self.soup = BeautifulSoup(response.read())

	def scrape(self):
		innings_tr_list = self.soup.find_all("tr", "data1")
		td_tags_names = ["runs", "minutes", "balls", "fours", "sixes", ]
		for	index in range(1,len(innings_tr_list)):
			data_tags = innings_tr_list.find_all("td")

		
	
