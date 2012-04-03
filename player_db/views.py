# Create your views here.
from  django.http import HttpResponse
from player_db.utils import ProfileScraper
from player_db.models import Player
import json

#view method for adding a player's stats at url to the DB
def player_add(request, cric_info_id):
	scraper = ProfileScraper(cric_info_id)
	
	return HttpResponse(json.dumps(scraper.scrape_profile()))