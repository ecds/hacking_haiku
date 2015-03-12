# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Role.notes'
        db.add_column(u'people_role', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Role.notes'
        db.delete_column(u'people_role', 'notes')


    models = {
        u'people.group': {
            'Meta': {'ordering': "['name']", 'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'people.name': {
            'Meta': {'object_name': 'Name'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'japanese_personal_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'roman_family_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'roman_personal_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'people.penname': {
            'Meta': {'object_name': 'PenName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'people.person': {
            'Meta': {'ordering': "['roman_family_name', 'roman_personal_name']", 'unique_together': "(('roman_family_name', 'roman_personal_name'),)", 'object_name': 'Person'},
            'birth_japanese': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'birth_roman': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'death_japanese': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'death_roman': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['people.Group']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'japanese_personal_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['people.Role']", 'null': 'True', 'blank': 'True'}),
            'roman_family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'roman_personal_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'people.role': {
            'Meta': {'ordering': "['name']", 'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['people']