# Create your views here.
from  django.http import HttpResponse
from player_db.utils import ProfileScraper, SquadScraper
from player_db.models import Player, BattingStat
from django.db import transaction
import json, re

#view method for adding a player's stats at url to the DB

@transaction.commit_on_success
def player_add(request, cric_info_id):

	if(len(Player.objects.filter(cricinfo_id=cric_info_id)) == 0):
		#means the player's not in our database
		scraper = ProfileScraper(cric_info_id)
		profile_info = scraper.scrape_profile()

		new_player_object = Player.create_player(profile_info["player_info"], cric_info_id)
		returnVal = ""
		
		if(new_player_object.id != None):
			for batting_stat_row in profile_info["batting_stats"]:
				
				batting_stat_obj = BattingStat.create_batting_stat(batting_stat_row, new_player_object)

				if(batting_stat_obj.id == None):
					return HttpResponse("something went wrong parsing " + json.dumps(batting_stat_row))

				

			return HttpResponse(returnVal)
		else:
			return HttpResponse("error scraping profile")

	else:
		return HttpResponse("We already had him")


## Pass this method an IPL team name (one of those defined in SquadScraper.scrape_squad)
## and it will scrap the squad Yahoo pipe for the players and add them all into the database
@transaction.commit_on_success
def scrape_squad(request, team_name):
	scraper = SquadScraper()

	cricinfo_ids = scraper.scrape_entire_squad(team_name)
	for id in cricinfo_ids:
		if(len(Player.objects.filter(cricinfo_id=id)) == 0):
			profile_scraper = ProfileScraper(id)
			profile_info = profile_scraper.scrape_profile()

			new_player_object = Player.create_player(profile_info["player_info"], id)

			if(new_player_object.id != None):
				for batting_stat_row in profile_info["batting_stats"]:
				
					batting_stat_obj = BattingStat.create_batting_stat(batting_stat_row, new_player_object)

					if(batting_stat_obj.id == None):
						return HttpResponse("something went wrong parsing " + json.dumps(batting_stat_row))


	return HttpResponse(scraper.scrape_entire_squad(team_name))