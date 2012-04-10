# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BattingStats'
        db.create_table('player_db_battingstats', (
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
        db.send_create_signal('player_db', ['BattingStats'])

        # Adding field 'Player.cricinfo_id'
        db.add_column('player_db_player', 'cricinfo_id', self.gf('django.db.models.fields.CharField')(default='', max_length=6), keep_default=False)

        # Adding field 'Player.player_country'
        db.add_column('player_db_player', 'player_country', self.gf('django.db.models.fields.CharField')(default='', max_length=30), keep_default=False)

        # Adding field 'Player.ipl_total_money_spent'
        db.add_column('player_db_player', 'ipl_total_money_spent', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'BattingStats'
        db.delete_table('player_db_battingstats')

        # Deleting field 'Player.cricinfo_id'
        db.delete_column('player_db_player', 'cricinfo_id')

        # Deleting field 'Player.player_country'
        db.delete_column('player_db_player', 'player_country')

        # Deleting field 'Player.ipl_total_money_spent'
        db.delete_column('player_db_player', 'ipl_total_money_spent')


    models = {
        'player_db.battingstats': {
            'Meta': {'object_name': 'BattingStats'},
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
