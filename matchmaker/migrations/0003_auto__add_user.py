# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'matchmaker_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matchmaker.Team'])),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'matchmaker', ['User'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'matchmaker_user')


    models = {
        u'matchmaker.team': {
            'Meta': {'object_name': 'Team'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'matchmaker.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['matchmaker.Team']"})
        }
    }

    complete_apps = ['matchmaker']