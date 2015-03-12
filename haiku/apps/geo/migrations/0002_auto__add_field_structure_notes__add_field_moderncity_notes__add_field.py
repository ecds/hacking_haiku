# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Structure.notes'
        db.add_column(u'geo_structure', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'ModernCity.notes'
        db.add_column(u'geo_moderncity', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Area.notes'
        db.add_column(u'geo_area', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Province.notes'
        db.add_column(u'geo_province', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'City.notes'
        db.add_column(u'geo_city', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'ModernPrefecture.notes'
        db.add_column(u'geo_modernprefecture', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'ModernArea.notes'
        db.add_column(u'geo_modernarea', 'notes',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Structure.notes'
        db.delete_column(u'geo_structure', 'notes')

        # Deleting field 'ModernCity.notes'
        db.delete_column(u'geo_moderncity', 'notes')

        # Deleting field 'Area.notes'
        db.delete_column(u'geo_area', 'notes')

        # Deleting field 'Province.notes'
        db.delete_column(u'geo_province', 'notes')

        # Deleting field 'City.notes'
        db.delete_column(u'geo_city', 'notes')

        # Deleting field 'ModernPrefecture.notes'
        db.delete_column(u'geo_modernprefecture', 'notes')

        # Deleting field 'ModernArea.notes'
        db.delete_column(u'geo_modernarea', 'notes')


    models = {
        u'geo.area': {
            'Meta': {'ordering': "['roman_name']", 'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modern_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.ModernArea']", 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.city': {
            'Meta': {'ordering': "['roman_name']", 'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modern_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.ModernCity']", 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Province']", 'null': 'True', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.modernarea': {
            'Meta': {'ordering': "['roman_name']", 'object_name': 'ModernArea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.moderncity': {
            'Meta': {'ordering': "['roman_name']", 'object_name': 'ModernCity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'prefecture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.ModernPrefecture']", 'null': 'True', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.modernprefecture': {
            'Meta': {'ordering': "['roman_name']", 'object_name': 'ModernPrefecture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.province': {
            'Meta': {'ordering': "['roman_name']", 'object_name': 'Province'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modern_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.ModernPrefecture']", 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.structure': {
            'Meta': {'ordering': "['roman_name']", 'object_name': 'Structure'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.City']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Province']", 'null': 'True', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'z_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        }
    }

    complete_apps = ['geo']