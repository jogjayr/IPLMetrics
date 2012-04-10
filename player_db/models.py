from django.db import models
from datetime import date
import re


GAME_TYPE = (
	("Tests", "Test Matches"),
	("ODIs", "One-day Internationals"),
	("T20Is", "Twenty20 International"),
	("First-class", "First-class"),
	("List A", "List A"),
	("Twenty20", "T20")
)

INTERNATIONAL_TEAMS = (
	("Afghanistan", "Afghanistan"),
	("Australia", "Australia"),
	("Bangladesh", "Bangladesh"),
	("Bermuda", "Bermuda"),
	("Canada", "Canada"),
	("England", "England"),
	("France", "France"),
	("Germany", "Germany"),
	("Holland", "Holland"),
	("India", "India"),
	("Ireland", "Ireland"),
	("Italy", "Italy"),
	("Kenya", "Kenya"),
	("Namibia", "Namibia"),
	("New Zealand", "New Zealand"),
	("Pakistan", "Pakistan"),
	("Sri Lanka", "Sri Lanka"),
	("USA", "USA"),
	("West Indies", "West Indies"),
	("Zimbabwe", "Zimbabwe")
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

	@staticmethod
	def create_player(profile_info, cric_info_id):
		new_player_object = Player(first_name=profile_info["FirstName"], 
			middle_name=profile_info["MiddleName"], 
			last_name=profile_info["LastName"], 
			date_of_birth=profile_info["DateOfBirth"],
			player_country=profile_info["Country"],
			cricinfo_id=cric_info_id)
		new_player_object.save()
		return new_player_object

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
	game_type = models.CharField(max_length="20", choices=GAME_TYPE)
	player = models.ForeignKey(Player)

	def get_values_list(self):
		return [self.matches_played ,
	self.innings_batted ,
	self.not_outs ,
	self.runs_scored ,
	self.high_score ,
	self.batting_average ,
	self.balls_faced ,
	self.batting_strike_rate ,
	self.centuries ,
	self.fifties ,
	self.fours ,
	self.sixes ,
	self.game_type ,
	self.player ]
	
	@staticmethod
	def create_batting_stat(batting_stat_row, new_player_object):
		batting_stat_obj = BattingStat( matches_played = int(batting_stat_row["Matches"]),
										innings_batted = int(batting_stat_row["Innings"]),
										# not_outs = int(re.sub("\D", "", batting_stat_row["NotOuts"])),
										not_outs = int(batting_stat_row["NotOuts"]),
										runs_scored = int(batting_stat_row["Runs"]),
										# high_score = int(re.sub("\D", "", batting_stat_row["HighScore"])),
										high_score =  int(batting_stat_row["HighScore"]),
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

		return batting_stat_obj



#Used to model every single innings played by a player
class Inning(models.Model):
	ALL_TEAMS = INTERNATIONAL_TEAMS + IPL_TEAMS
	player = models.ForeignKey(Player)
	runs_scored = models.IntegerField(default=0)
	balls_faced = models.IntegerField(default=0)
	was_out = models.BooleanField(default=True)
	position = models.IntegerField(default=1,null=True)
	fours = models.IntegerField(default=0)
	sixes = models.IntegerField(default=0)
	minutes_batted = models.IntegerField(default=0)
	opposition = models.CharField(max_length=30, choices=ALL_TEAMS)
	player_team = models.CharField(max_length=30, choices=ALL_TEAMS, null=True)
	date = models.DateField(null=True, default=date(3000, 12, 12))
	match_result = models.CharField(max_length=4, choices=(("Win", "Win"), ("Lose", "Lose"), ("Draw", "Draw"), ("Tie", "Tie")), null=True)
	game_type = models.CharField(max_length="20", choices=GAME_TYPE)

	@staticmethod
	def create_inning(inning_row, new_player_object):
		inning_obj = Inning( runs_scored = inning_row["runs"],
							 balls_faced = inning_row["balls"],
							 was_out = inning_row["was_out"],
							 fours = inning_row["fours"],
							 sixes = inning_row["sixes"],
							 minutes_batted = inning_row["minutes"],
							 opposition = inning_row["opposition"],
							 date = inning_row["date"],
							 game_type = inning_row["Type"])
		inning_obj.player = new_player_object
		inning_obj.save()
		return inning_obj
