# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Verse.author'
        db.alter_column(u'texts_verse', 'author_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Verse.author'
        raise RuntimeError("Cannot reverse this migration. 'Verse.author' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Verse.author'
        db.alter_column(u'texts_verse', 'author_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person']))

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
        },
        u'people.group': {
            'Meta': {'ordering': "['name']", 'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
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
        },
        u'texts.altverse': {
            'Meta': {'ordering': "['japanese_text']", 'object_name': 'AltVerse'},
            'english_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_text': ('django.db.models.fields.TextField', [], {}),
            'romanization': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'verse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['texts.Verse']"})
        },
        u'texts.kigo': {
            'Meta': {'ordering': "['japanese']", 'object_name': 'Kigo'},
            'english': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'romanization': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'texts.verse': {
            'Meta': {'ordering': "['author', 'japanese_text']", 'object_name': 'Verse'},
            'allusions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'allusions'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['texts.Work']"}),
            'areas': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['geo.Area']", 'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']", 'null': 'True', 'blank': 'True'}),
            'cities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['geo.City']", 'null': 'True', 'blank': 'True'}),
            'encounters': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'encounters'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['people.Person']"}),
            'english_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_date': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'japanese_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'kigo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['texts.Kigo']", 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'other_works': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'other_works'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['texts.Work']"}),
            'provinces': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['geo.Province']", 'null': 'True', 'blank': 'True'}),
            'roman_date': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'romanization': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'structures': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['geo.Structure']", 'null': 'True', 'blank': 'True'}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['texts.Work']", 'null': 'True', 'blank': 'True'})
        },
        u'texts.work': {
            'Meta': {'ordering': "['english_title']", 'object_name': 'Work'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['people.Person']", 'null': 'True', 'blank': 'True'}),
            'english_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_date': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'japanese_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'roman_date': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'romanized_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['texts']