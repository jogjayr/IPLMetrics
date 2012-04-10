# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Innings'
        db.delete_table('player_db_innings')

        # Deleting model 'BattingStats'
        db.delete_table('player_db_battingstats')

        # Adding model 'Inning'
        db.create_table('player_db_inning', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['player_db.Player'])),
            ('runs_scored', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('balls_faced', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('was_out', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fours', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sixes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('minutes_batted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('opposition', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('game_type', self.gf('django.db.models.fields.CharField')(max_length='10')),
        ))
        db.send_create_signal('player_db', ['Inning'])

        # Adding model 'BattingStat'
        db.create_table('player_db_battingstat', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('matches_played', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('innings_batted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('not_outs', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('runs_scored', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('high_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('batting_average', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('balls_faced', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('batting_strike_rate', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('centuries', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fifties', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fours', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sixes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('game_type', self.gf('django.db.models.fields.CharField')(max_length='10')),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['player_db.Player'])),
        ))
        db.send_create_signal('player_db', ['BattingStat'])


    def backwards(self, orm):
        
        # Adding model 'Innings'
        db.create_table('player_db_innings', (
            ('fours', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('minutes_batted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['player_db.Player'])),
            ('runs_scored', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('opposition', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sixes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('game_type', self.gf('django.db.models.fields.CharField')(max_length='10')),
            ('balls_faced', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('was_out', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('player_db', ['Innings'])

        # Adding model 'BattingStats'
        db.create_table('player_db_battingstats', (
            ('sixes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('centuries', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('batting_average', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('high_score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('batting_strike_rate', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('fours', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('innings_batted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('game_type', self.gf('django.db.models.fields.CharField')(max_length='10')),
            ('matches_played', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['player_db.Player'])),
            ('balls_faced', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('runs_scored', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fifties', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('not_outs', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('player_db', ['BattingStats'])

        # Deleting model 'Inning'
        db.delete_table('player_db_inning')

        # Deleting model 'BattingStat'
        db.delete_table('player_db_battingstat')


    models = {
        'player_db.battingstat': {
            'Meta': {'object_name': 'BattingStat'},
            'balls_faced': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'batting_average': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'batting_strike_rate': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'centuries': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fifties': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fours': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'game_type': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
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
            'game_type': ('django.db.models.fields.CharField', [], {'max_length': "'10'"}),
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
            'player_country': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        }
    }

    complete_apps = ['player_db']
