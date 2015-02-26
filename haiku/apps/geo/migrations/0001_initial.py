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
            ('japanese_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('roman_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('x_coordinate', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=12, blank=True)),
            ('y_coordinate', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=12, blank=True)),
        ))
        db.send_create_signal(u'geo', ['ModernPrefecture'])

        # Adding model 'Province'
        db.create_table(u'geo_province', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('roman_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('modern_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.ModernPrefecture'], null=True, blank=True)),
            ('x_coordinate', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=12, blank=True)),
            ('y_coordinate', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=12, blank=True)),
        ))
        db.send_create_signal(u'geo', ['Province'])

        # Adding model 'ModernCity'
        db.create_table(u'geo_moderncity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('roman_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('prefecture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.ModernPrefecture'], null=True, blank=True)),
            ('x_coordinate', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=12, blank=True)),
            ('y_coordinate', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=12, blank=True)),
        ))
        db.send_create_signal(u'geo', ['ModernCity'])

        # Adding model 'City'
        db.create_table(u'geo_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('roman_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('modern_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.ModernCity'], null=True, blank=True)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.Province'], null=True, blank=True)),
            ('x_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('y_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
        ))
        db.send_create_signal(u'geo', ['City'])

        # Adding model 'Structure'
        db.create_table(u'geo_structure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('roman_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.City'], null=True, blank=True)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geo.Province'], null=True, blank=True)),
            ('x_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('y_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
            ('z_coordinate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=12, blank=True)),
        ))
        db.send_create_signal(u'geo', ['Structure'])


    def backwards(self, orm):
        # Deleting model 'ModernPrefecture'
        db.delete_table(u'geo_modernprefecture')

        # Deleting model 'Province'
        db.delete_table(u'geo_province')

        # Deleting model 'ModernCity'
        db.delete_table(u'geo_moderncity')

        # Deleting model 'City'
        db.delete_table(u'geo_city')

        # Deleting model 'Structure'
        db.delete_table(u'geo_structure')


    models = {
        u'geo.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modern_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.ModernCity']", 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Province']", 'null': 'True', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.moderncity': {
            'Meta': {'object_name': 'ModernCity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prefecture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.ModernPrefecture']", 'null': 'True', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.modernprefecture': {
            'Meta': {'object_name': 'ModernPrefecture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.province': {
            'Meta': {'object_name': 'Province'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modern_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.ModernPrefecture']", 'null': 'True', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.structure': {
            'Meta': {'object_name': 'Structure'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.City']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Province']", 'null': 'True', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'z_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        }
    }

    complete_apps = ['geo']