# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FaqEntry'
        db.create_table('cmsplugin_faqentry', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('css', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('faq', ['FaqEntry'])

        # Adding model 'FaqList'
        db.create_table('cmsplugin_faqlist', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('truncate_body', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=5)),
            ('show_body', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('css', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('faq', ['FaqList'])


    def backwards(self, orm):
        # Deleting model 'FaqEntry'
        db.delete_table('cmsplugin_faqentry')

        # Deleting model 'FaqList'
        db.delete_table('cmsplugin_faqlist')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'faq.faqentry': {
            'Meta': {'object_name': 'FaqEntry', 'db_table': "'cmsplugin_faqentry'"},
            'body': ('django.db.models.fields.TextField', [], {}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'css': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'faq.faqlist': {
            'Meta': {'object_name': 'FaqList', 'db_table': "'cmsplugin_faqlist'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'css': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'show_body': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'truncate_body': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '5'})
        }
    }

    complete_apps = ['faq']