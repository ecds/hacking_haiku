# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ModernPrefecture'
        db.create_table(u'geo_modernprefecture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('roman_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('x_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('y_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'geo', ['ModernPrefecture'])

        # Adding model 'Province'
        db.create_table(u'geo_province', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('roman_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('modern_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.ModernPrefecture'], null=True, blank=True)),
            ('x_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('y_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'geo', ['Province'])

        # Adding model 'ModernCity'
        db.create_table(u'geo_moderncity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('roman_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('prefecture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.ModernPrefecture'], null=True, blank=True)),
            ('x_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('y_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'geo', ['ModernCity'])

        # Adding model 'City'
        db.create_table(u'geo_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('roman_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('modern_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.ModernCity'], null=True, blank=True)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.Province'], null=True, blank=True)),
            ('x_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('y_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'geo', ['City'])

        # Adding model 'ModernArea'
        db.create_table(u'geo_modernarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('roman_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('x_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('y_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'geo', ['ModernArea'])

        # Adding model 'Area'
        db.create_table(u'geo_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('roman_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('modern_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.ModernArea'], null=True, blank=True)),
            ('x_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('y_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'geo', ['Area'])

        # Adding model 'Structure'
        db.create_table(u'geo_structure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('roman_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.City'], null=True, blank=True)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.Province'], null=True, blank=True)),
            ('x_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('y_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('z_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'geo', ['Structure'])

        # Adding model 'Stop'
        db.create_table(u'geo_stop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.City'], null=True, blank=True)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.Province'], null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.Area'], null=True, blank=True)),
            ('structure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.Structure'], null=True, blank=True)),
            ('japanese_date', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('roman_date', self.gf('django_date_extensions.fields.ApproximateDateField')(max_length=10, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'geo', ['Stop'])

        # Adding model 'StopVerse'
        db.create_table(u'geo_stopverse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.Stop'])),
            ('verse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['texts.Verse'])),
        ))
        db.send_create_signal(u'geo', ['StopVerse'])


    def backwards(self, orm):
        # Deleting model 'ModernPrefecture'
        db.delete_table(u'geo_modernprefecture')

        # Deleting model 'Province'
        db.delete_table(u'geo_province')

        # Deleting model 'ModernCity'
        db.delete_table(u'geo_moderncity')

        # Deleting model 'City'
        db.delete_table(u'geo_city')

        # Deleting model 'ModernArea'
        db.delete_table(u'geo_modernarea')

        # Deleting model 'Area'
        db.delete_table(u'geo_area')

        # Deleting model 'Structure'
        db.delete_table(u'geo_structure')

        # Deleting model 'Stop'
        db.delete_table(u'geo_stop')

        # Deleting model 'StopVerse'
        db.delete_table(u'geo_stopverse')


    models = {
        u'geo.area': {
            'Meta': {'ordering': "['roman_name']", 'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modern_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.ModernArea']", 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
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
            'roman_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.modernarea': {
            'Meta': {'ordering': "['roman_name']", 'object_name': 'ModernArea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.moderncity': {
            'Meta': {'ordering': "['roman_name']", 'object_name': 'ModernCity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'prefecture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.ModernPrefecture']", 'null': 'True', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.modernprefecture': {
            'Meta': {'ordering': "['roman_name']", 'object_name': 'ModernPrefecture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.province': {
            'Meta': {'ordering': "['roman_name']", 'object_name': 'Province'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modern_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.ModernPrefecture']", 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.stop': {
            'Meta': {'ordering': "['order']", 'object_name': 'Stop'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Area']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.City']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_date': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Province']", 'null': 'True', 'blank': 'True'}),
            'roman_date': ('django_date_extensions.fields.ApproximateDateField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Structure']", 'null': 'True', 'blank': 'True'})
        },
        u'geo.stopverse': {
            'Meta': {'object_name': 'StopVerse'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Stop']"}),
            'verse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['texts.Verse']"})
        },
        u'geo.structure': {
            'Meta': {'ordering': "['roman_name']", 'object_name': 'Structure'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.City']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Province']", 'null': 'True', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
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

    complete_apps = ['geo']