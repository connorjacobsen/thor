# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Article', fields ['full_URL']
        db.create_unique(u'succinctly_article', ['full_URL'])


    def backwards(self, orm):
        # Removing unique constraint on 'Article', fields ['full_URL']
        db.delete_unique(u'succinctly_article', ['full_URL'])


    models = {
        u'succinctly.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'full_URL': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'home_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['succinctly.Website']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'summary': ('django.db.models.fields.TextField', [], {'max_length': '140'}),
            'webpage_name': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        u'succinctly.website': {
            'Meta': {'object_name': 'Website'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_image_url': ('django.db.models.fields.URLField', [], {'max_length': '254'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254'})
        }
    }

    complete_apps = ['succinctly']