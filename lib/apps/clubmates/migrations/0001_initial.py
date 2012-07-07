# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('clubmates_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=254)),
        ))
        db.send_create_signal('clubmates', ['User'])

        # Adding model 'Location'
        db.create_table('clubmates_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clubmates.Location'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('clubmates', ['Location'])

        # Adding model 'Message'
        db.create_table('clubmates_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clubmates.User'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clubmates.Location'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('in_reply_to', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clubmates.Message'], null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal('clubmates', ['Message'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table('clubmates_user')

        # Deleting model 'Location'
        db.delete_table('clubmates_location')

        # Deleting model 'Message'
        db.delete_table('clubmates_message')


    models = {
        'clubmates.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clubmates.Location']", 'null': 'True', 'blank': 'True'})
        },
        'clubmates.message': {
            'Meta': {'object_name': 'Message'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_reply_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clubmates.Message']", 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clubmates.Location']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clubmates.User']"})
        },
        'clubmates.user': {
            'Meta': {'object_name': 'User'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['clubmates']