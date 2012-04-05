from django.conf.urls import patterns, include, url


urlpatterns = patterns("player_db.views",
	url(r'^player_add/(?P<cric_info_id>\d+)/$', "player_add"),
	url(r'^scrape_squad/(?P<team_name>\w+)/$', "scrape_squad"),
	url(r'^test_batting/$', "test_batting_records"),
	url(r'^odi_batting/$', "odi_batting_records"),
	url(r'^t20i_batting/$', "t20i_batting_records"),
	url(r'^fc_batting/$', "first_class_batting_records"),
	url(r'^lista_batting/$', "list_a_batting_records"),
	url(r'^t20_batting/$', "t20_batting_records")
)