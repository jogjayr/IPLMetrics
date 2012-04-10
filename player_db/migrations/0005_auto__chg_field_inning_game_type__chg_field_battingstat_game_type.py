# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Inning.game_type'
        db.alter_column('player_db_inning', 'game_type', self.gf('django.db.models.fields.CharField')(max_length='20'))

        # Changing field 'BattingStat.game_type'
        db.alter_column('player_db_battingstat', 'game_type', self.gf('django.db.models.fields.CharField')(max_length='20'))


    def backwards(self, orm):
        
        # Changing field 'Inning.game_type'
        db.alter_column('player_db_inning', 'game_type', self.gf('django.db.models.fields.CharField')(max_length='10'))

        # Changing field 'BattingStat.game_type'
        db.alter_column('player_db_battingstat', 'game_type', self.gf('django.db.models.fields.CharField')(max_length='10'))


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
            'date': ('django.db.models.fields.DateField', [], {}),
            'fours': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'game_type': ('django.db.models.fields.CharField', [], {'max_length': "'20'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minutes_batted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'opposition': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['player_db.Player']"}),
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
