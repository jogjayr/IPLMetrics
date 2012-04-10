# Create your views here.
from  django.http import HttpResponse
from player_db.utils import ProfileScraper, SquadScraper
from player_db.models import Player, BattingStat
from django.db import transaction
from django.views.generic import TemplateView
import json, re, csv



class IndexView(TemplateView):
	template_name = "index.html"

#view method for adding a player's stats at url to the DB

@transaction.commit_on_success
def player_add(request, cric_info_id):

	# if(len(Player.objects.filter(cricinfo_id=cric_info_id)) == 0):
		#means the player's not in our database
		scraper = ProfileScraper(cric_info_id)
		profile_info = scraper.scrape_profile()

		# new_player_object = Player.create_player(profile_info["player_info"], cric_info_id)
		returnVal = ""
		
		if(new_player_object.id != None):
			for batting_stat_row in profile_info["batting_stats"]:
				
				batting_stat_obj = BattingStat.create_batting_stat(batting_stat_row, new_player_object)

				if(batting_stat_obj.id == None):
					return HttpResponse("something went wrong parsing " + json.dumps(batting_stat_row))

				

			return HttpResponse(json.dumps(profile_info))
		else:
			return HttpResponse("error scraping profile")

	# else:
	# 	return HttpResponse("We already had him")


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


## Returns CSV formatted Test records of the entire player_db
## Why CSV? Because that's what we need right now. Later, we can talk
## about something more refined

## #short-termismatwork
def test_batting_records(request):
	response = HttpResponse(mimetype="text/csv")
	response['Content-disposition'] = 'attachment; filename=test_records.csv'

	writer = csv.writer(response)
	test_batting_records = BattingStat.objects.filter(game_type="Tests").select_related()

	for record in test_batting_records:
		writer.writerow([record.player.first_name + " " + record.player.last_name] + record.get_values_list()[:13])

	return response

def odi_batting_records(request):
	response = HttpResponse(mimetype="text/csv")
	response['Content-disposition'] = 'attachment; filename=odi_records.csv'

	writer = csv.writer(response)
	test_batting_records = BattingStat.objects.filter(game_type="ODIs").select_related()

	for record in test_batting_records:
		writer.writerow([record.player.first_name + " " + record.player.last_name] + record.get_values_list()[:13])

	return response

def t20i_batting_records(request):
	response = HttpResponse(mimetype="text/csv")
	response['Content-disposition'] = 'attachment; filename=t20i_records.csv'

	writer = csv.writer(response)
	test_batting_records = BattingStat.objects.filter(game_type="T20Is").select_related()

	for record in test_batting_records:
		writer.writerow([record.player.first_name + " " + record.player.last_name] + record.get_values_list()[:13])

	return response

def first_class_batting_records(request):
	response = HttpResponse(mimetype="text/csv")
	response['Content-disposition'] = 'attachment; filename=first_class_records.csv'

	writer = csv.writer(response)
	test_batting_records = BattingStat.objects.filter(game_type="First-class").select_related()

	for record in test_batting_records:
		writer.writerow([record.player.first_name + " " + record.player.last_name] + record.get_values_list()[:13])

	return response

def list_a_batting_records(request):
	response = HttpResponse(mimetype="text/csv")
	response['Content-disposition'] = 'attachment; filename=list_a_records.csv'

	writer = csv.writer(response)
	test_batting_records = BattingStat.objects.filter(game_type="List A").select_related()

	for record in test_batting_records:
		writer.writerow([record.player.first_name + " " + record.player.last_name] + record.get_values_list()[:13])

	return response

def t20_batting_records(request):
	response = HttpResponse(mimetype="text/csv")
	response['Content-disposition'] = 'attachment; filename=t20_records.csv'

	writer = csv.writer(response)
	test_batting_records = BattingStat.objects.filter(game_type="Twenty20").select_related()

	for record in test_batting_records:
		writer.writerow([record.player.first_name + " " + record.player.last_name] + record.get_values_list()[:13])

	return response