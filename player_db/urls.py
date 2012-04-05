from django.conf.urls import patterns, include, url


urlpatterns = patterns("player_db.views",
	url(r'^player_add/(?P<cric_info_id>\d+)/$', "player_add"),
	url(r'^scrape_squad/(?P<team_name>\w+)/$', "scrape_squad")
)