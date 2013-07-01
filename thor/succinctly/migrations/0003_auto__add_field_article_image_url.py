# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.image_url'
        db.add_column(u'succinctly_article', 'image_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=254, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.image_url'
        db.delete_column(u'succinctly_article', 'image_url')


    models = {
        u'succinctly.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'full_URL': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'summary': ('django.db.models.fields.TextField', [], {'max_length': '140'}),
            'webpage_name': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        }
    }

    complete_apps = ['succinctly']