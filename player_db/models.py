from django.db import models

GAME_TYPE = (
	("Test", "Test Matches"),
	("ODI", "One-day Internationals"),
	("IPL", "Indian Premier League")
)

INTERNATIONAL_TEAMS = (
	("AFG", "Afghanistan"),
	("AUS", "Australia"),
	("BAN", "Bangladesh"),
	("BER", "Bermuda"),
	("CAN", "Canada"),
	("ENG", "England"),
	("FRA", "France"),
	("GER", "Germany"),
	("HOL", "Holland"),
	("IND", "India"),
	("IRL", "Ireland"),
	("ITL", "Italy"),
	("KEN", "Kenya"),
	("NAM", "Namibia"),
	("NZL", "New Zealand"),
	("PAK", "Pakistan"),
	("SRL", "Sri Lanka"),
	("USA", "USA"),
	("WIN", "West Indies"),
	("ZIM", "Zimbabwe")
)

IPL_TEAMS = (
	("CSK", "Chennai Super Kings"),
	("DC", "Deccan Chargers"),
	("DD", "Delhi Daredevils"),
	("KXP", "Kings XI Punjab"),
	("KKR", "Kolkata Knight Riders"),
	("MI", "Mumbai Indians"),
	("PW", "Pune Warriors"),
	("RR", "Rajasthan Royals"),
	("RCB", "Royal Challengers Bangalore")
)

# Create your models here.
class Player(models.Model):
	first_name = models.CharField(max_length=30, default = "")
	middle_name = models.CharField(max_length=30, default = "")
	last_name = models.CharField(max_length=30, default = "")
	date_of_birth = models.DateField()
	cricinfo_id = models.CharField(max_length=6, default = "")
	player_country = models.CharField(max_length=30, choices=INTERNATIONAL_TEAMS)
	ipl_total_money_spent = models.FloatField(default=0)




class BattingStat(models.Model):
	#batting stats
	matches_played = models.IntegerField(default=0)
	innings_batted = models.IntegerField(default=0)
	not_outs = models.IntegerField(default=0)
	runs_scored = models.IntegerField(default=0)
	high_score = models.IntegerField(default=0)
	batting_average = models.FloatField(default=0)
	balls_faced = models.IntegerField(default=0)
	batting_strike_rate = models.FloatField(default=0)
	centuries = models.IntegerField(default=0)
	fifties = models.IntegerField(default=0)
	fours = models.IntegerField(default=0)
	sixes = models.IntegerField(default=0)
	game_type = models.CharField(max_length="10", choices=GAME_TYPE)
	player = models.ForeignKey(Player)

#Used to model every single innings played by a player
class Inning(models.Model):
	OPPOSITION = INTERNATIONAL_TEAMS + IPL_TEAMS
	player = models.ForeignKey(Player)
	runs_scored = models.IntegerField(default=0)
	balls_faced = models.IntegerField(default=0)
	was_out = models.BooleanField(default=True)
	fours = models.IntegerField(default=0)
	sixes = models.IntegerField(default=0)
	minutes_batted = models.IntegerField(default=0)
	opposition = models.CharField(max_length=30, choices=OPPOSITION)
	date = models.DateField()
	game_type = models.CharField(max_length="10", choices=GAME_TYPE)

	# test_matches_played = models.IntegerField(default=0)
	# test_innings_batted = models.IntegerField(default=0)
	# test_not_outs = models.IntegerField(default=0)
	# test_runs_scored = models.IntegerField(default=0)
	# test_high_score = models.IntegerField(default=0)
	# test_batting_average = models.FloatField()
	# test_balls_faced = models.IntegerField(default=0)
	# test_batting_strike_rate = models.FloatField()
	# test_centuries = models.IntegerField(default=0)
	# test_fifties = models.IntegerField(default=0)
	# test_fours = models.IntegerField(default=0)
	# test_sixes = models.IntegerField(default=0)

	# odi_matches_played = models.IntegerField(default=0)
	# odi_innings_batted = models.IntegerField(default=0)
	# odi_not_outs = models.IntegerField(default=0)
	# odi_runs_scored = models.IntegerField()
	# odi_high_score = models.IntegerField()
	# odi_batting_average = models.FloatField()
	# odi_balls_faced = models.IntegerField()
	# odi_batting_strike_rate = models.FloatField()
	# odi_centuries = models.IntegerField()
	# odi_fifties = models.IntegerField()
	# odi_fours = models.IntegerField()
	# odi_sixes = models.IntegerField()

	# #bowling stats
	# ipl_innings_bowled = models.IntegerField()
	# ipl_balls_bowled = models.IntegerField()
	# ipl_maidens_bowled = models.IntegerField()
	# ipl_runs_conceded = models.IntegerField()
	# ipl_wickets_taken = models.IntegerField()
	# ipl_best_bowling = models.CommaSeparatedIntegerField(max_length=2)
	# ipl_bowling_average = models.FloatField()
	# ipl_economy_rate = models.FloatField()
	# ipl_bowling_strike_rate = models.FloatField()
	# ipl_four_wicket_hauls = models.IntegerField()
	# ipl_five_wicket_hauls = models.IntegerField()


	# test_innings_bowled = models.IntegerField()
	# test_balls_bowled = models.IntegerField()
	# test_maidens_bowled = models.IntegerField()
	# test_runs_conceded = models.IntegerField()
	# test_wickets_taken = models.IntegerField()
	# test_best_bowling = models.CommaSeparatedIntegerField(max_length=2)
	# test_bowling_average = models.FloatField()
	# test_economy_rate = models.FloatField()
	# test_bowling_strike_rate = models.FloatField()
	# test_five_wicket_hauls = models.IntegerField()
	# test_ten_wicket_hauls = models.IntegerField()
	

	# odi_innings_bowled = models.IntegerField()
	# odi_balls_bowled = models.IntegerField()
	# odi_maidens_bowled = models.IntegerField()
	# odi_runs_conceded = models.IntegerField()
	# odi_wickets_taken = models.IntegerField()
	# odi_best_bowling = models.CommaSeparatedIntegerField(max_length=2)
	# odi_bowling_average = models.FloatField()
	# odi_economy_rate = models.FloatField()
	# odi_bowling_strike_rate = models.FloatField()
	# odi_five_wicket_hauls = models.IntegerField()
	# odi_ten_wicket_hauls = models.IntegerField()
	
