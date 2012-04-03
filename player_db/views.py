# Create your views here.
from  django.http import HttpResponse
from player_db.utils import ProfileScraper
from player_db.models import Player, BattingStat
import json, re

#view method for adding a player's stats at url to the DB
def player_add(request, cric_info_id):

	if(len(Player.objects.filter(cricinfo_id=cric_info_id)) == 0):
		#means the player's not in our database
		scraper = ProfileScraper(cric_info_id)
		profile_info = scraper.scrape_profile()

		new_player_object = Player(first_name=profile_info["player_info"]["FirstName"], 
			middle_name=profile_info["player_info"]["MiddleName"], 
			last_name=profile_info["player_info"]["LastName"], 
			date_of_birth=profile_info["player_info"]["DateOfBirth"], 
			cricinfo_id=cric_info_id)

		returnVal = ""
		new_player_object.save()
		if(new_player_object.id != None):
			for batting_stat_row in profile_info["batting_stats"]:
				batting_stat_obj = BattingStat( matches_played = int(batting_stat_row["Matches"]),
												innings_batted = int(batting_stat_row["Innings"]),
												not_outs = int(re.sub("\D", "", batting_stat_row["NotOuts"])),
												runs_scored = int(batting_stat_row["Runs"]),
												high_score = int(re.sub("\D", "", batting_stat_row["HighScore"])),
												batting_average = float(batting_stat_row["Average"]),
												balls_faced = int(batting_stat_row["BallsFaced"]),
												batting_strike_rate = float(batting_stat_row["StrikeRate"]),
												centuries = int(batting_stat_row["Centuries"]),
												fifties = int(batting_stat_row["Fifties"]),
												fours = int(batting_stat_row["Fours"]),
												sixes = int(batting_stat_row["Sixes"]),
												game_type = batting_stat_row["Type"])
				batting_stat_obj.player = new_player_object;
				batting_stat_obj.save()

				if(batting_stat_obj.id == None):
					return HttpResponse("something went wrong parsing " + json.dumps(batting_stat_row))
				

			return HttpResponse(returnVal)
		else:
			return HttpResponse("error scraping profile")

	else:
		return HttpResponse("We already had him")