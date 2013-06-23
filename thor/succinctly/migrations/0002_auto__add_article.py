# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'succinctly_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_URL', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('summary', self.gf('django.db.models.fields.TextField')(max_length=140)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('webpage_name', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'succinctly', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'succinctly_article')


    models = {
        u'succinctly.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'full_URL': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'summary': ('django.db.models.fields.TextField', [], {'max_length': '140'}),
            'webpage_name': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        }
    }

    complete_apps = ['succinctly']