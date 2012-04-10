# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Inning.position'
        db.add_column('player_db_inning', 'position', self.gf('django.db.models.fields.IntegerField')(default=1, null=True), keep_default=False)

        # Adding field 'Inning.player_team'
        db.add_column('player_db_inning', 'player_team', self.gf('django.db.models.fields.CharField')(max_length=30, null=True), keep_default=False)

        # Adding field 'Inning.match_result'
        db.add_column('player_db_inning', 'match_result', self.gf('django.db.models.fields.CharField')(max_length=4, null=True), keep_default=False)

        # Changing field 'Inning.date'
        db.alter_column('player_db_inning', 'date', self.gf('django.db.models.fields.DateField')(null=True))


    def backwards(self, orm):
        
        # Deleting field 'Inning.position'
        db.delete_column('player_db_inning', 'position')

        # Deleting field 'Inning.player_team'
        db.delete_column('player_db_inning', 'player_team')

        # Deleting field 'Inning.match_result'
        db.delete_column('player_db_inning', 'match_result')

        # Changing field 'Inning.date'
        db.alter_column('player_db_inning', 'date', self.gf('django.db.models.fields.DateField')(default=datetime.date(3000, 12, 12)))


    models = {
        'player_db.battingstat': {
            'Meta': {'object_name': 'BattingStat'},
            'balls_faced': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'batting_average': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'batting_strike_rate': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centuries': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fifties': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fours': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'game_type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"}),
            'high_score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innings_batted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'matches_played': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'not_outs': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['player_db.Player']"}),
            'runs_scored': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sixes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'player_db.inning': {
            'Meta': {'object_name': 'Inning'},
            'balls_faced': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(3000, 12, 12)', 'null': 'True'}),
            'fours': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'game_type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match_result': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True'}),
            'minutes_batted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'opposition': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['player_db.Player']"}),
            'player_team': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True'}),
            'runs_scored': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sixes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'was_out': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'player_db.player': {
            'Meta': {'object_name': 'Player'},
            'cricinfo_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '6'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipl_total_money_spent': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'player_country': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['player_db']
