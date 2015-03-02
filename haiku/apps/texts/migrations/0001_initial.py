# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Kigo'
        db.create_table(u'texts_kigo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('english', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('romanization', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('season', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'texts', ['Kigo'])

        # Adding model 'Work'
        db.create_table(u'texts_work', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('english_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('romanized_title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('japanese_date', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('roman_date', self.gf('django_date_extensions.fields.ApproximateDateField')(max_length=10, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'texts', ['Work'])

        # Adding M2M table for field authors on 'Work'
        m2m_table_name = db.shorten_name(u'texts_work_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('work', models.ForeignKey(orm[u'texts.work'], null=False)),
            ('person', models.ForeignKey(orm[u'people.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['work_id', 'person_id'])

        # Adding model 'Verse'
        db.create_table(u'texts_verse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('english_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('romanization', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
            ('work', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['texts.Work'], null=True, blank=True)),
            ('japanese_date', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('roman_date', self.gf('django_date_extensions.fields.ApproximateDateField')(max_length=10, null=True, blank=True)),
            ('kigo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['texts.Kigo'], null=True, blank=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'texts', ['Verse'])

        # Adding M2M table for field other_works on 'Verse'
        m2m_table_name = db.shorten_name(u'texts_verse_other_works')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('verse', models.ForeignKey(orm[u'texts.verse'], null=False)),
            ('work', models.ForeignKey(orm[u'texts.work'], null=False))
        ))
        db.create_unique(m2m_table_name, ['verse_id', 'work_id'])

        # Adding M2M table for field encounters on 'Verse'
        m2m_table_name = db.shorten_name(u'texts_verse_encounters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('verse', models.ForeignKey(orm[u'texts.verse'], null=False)),
            ('person', models.ForeignKey(orm[u'people.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['verse_id', 'person_id'])

        # Adding M2M table for field structures on 'Verse'
        m2m_table_name = db.shorten_name(u'texts_verse_structures')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('verse', models.ForeignKey(orm[u'texts.verse'], null=False)),
            ('structure', models.ForeignKey(orm[u'geo.structure'], null=False))
        ))
        db.create_unique(m2m_table_name, ['verse_id', 'structure_id'])

        # Adding M2M table for field cities on 'Verse'
        m2m_table_name = db.shorten_name(u'texts_verse_cities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('verse', models.ForeignKey(orm[u'texts.verse'], null=False)),
            ('city', models.ForeignKey(orm[u'geo.city'], null=False))
        ))
        db.create_unique(m2m_table_name, ['verse_id', 'city_id'])

        # Adding M2M table for field provinces on 'Verse'
        m2m_table_name = db.shorten_name(u'texts_verse_provinces')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('verse', models.ForeignKey(orm[u'texts.verse'], null=False)),
            ('province', models.ForeignKey(orm[u'geo.province'], null=False))
        ))
        db.create_unique(m2m_table_name, ['verse_id', 'province_id'])

        # Adding M2M table for field areas on 'Verse'
        m2m_table_name = db.shorten_name(u'texts_verse_areas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('verse', models.ForeignKey(orm[u'texts.verse'], null=False)),
            ('area', models.ForeignKey(orm[u'geo.area'], null=False))
        ))
        db.create_unique(m2m_table_name, ['verse_id', 'area_id'])

        # Adding M2M table for field allusions on 'Verse'
        m2m_table_name = db.shorten_name(u'texts_verse_allusions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('verse', models.ForeignKey(orm[u'texts.verse'], null=False)),
            ('work', models.ForeignKey(orm[u'texts.work'], null=False))
        ))
        db.create_unique(m2m_table_name, ['verse_id', 'work_id'])

        # Adding model 'AltVerse'
        db.create_table(u'texts_altverse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_text', self.gf('django.db.models.fields.TextField')()),
            ('english_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('romanization', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('verse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['texts.Verse'])),
        ))
        db.send_create_signal(u'texts', ['AltVerse'])


    def backwards(self, orm):
        # Deleting model 'Kigo'
        db.delete_table(u'texts_kigo')

        # Deleting model 'Work'
        db.delete_table(u'texts_work')

        # Removing M2M table for field authors on 'Work'
        db.delete_table(db.shorten_name(u'texts_work_authors'))

        # Deleting model 'Verse'
        db.delete_table(u'texts_verse')

        # Removing M2M table for field other_works on 'Verse'
        db.delete_table(db.shorten_name(u'texts_verse_other_works'))

        # Removing M2M table for field encounters on 'Verse'
        db.delete_table(db.shorten_name(u'texts_verse_encounters'))

        # Removing M2M table for field structures on 'Verse'
        db.delete_table(db.shorten_name(u'texts_verse_structures'))

        # Removing M2M table for field cities on 'Verse'
        db.delete_table(db.shorten_name(u'texts_verse_cities'))

        # Removing M2M table for field provinces on 'Verse'
        db.delete_table(db.shorten_name(u'texts_verse_provinces'))

        # Removing M2M table for field areas on 'Verse'
        db.delete_table(db.shorten_name(u'texts_verse_areas'))

        # Removing M2M table for field allusions on 'Verse'
        db.delete_table(db.shorten_name(u'texts_verse_allusions'))

        # Deleting model 'AltVerse'
        db.delete_table(u'texts_altverse')


    models = {
        u'geo.area': {
            'Meta': {'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modern_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.ModernArea']", 'null': 'True', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modern_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.ModernCity']", 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Province']", 'null': 'True', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.modernarea': {
            'Meta': {'object_name': 'ModernArea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.moderncity': {
            'Meta': {'object_name': 'ModernCity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'prefecture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.ModernPrefecture']", 'null': 'True', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.modernprefecture': {
            'Meta': {'object_name': 'ModernPrefecture'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.province': {
            'Meta': {'object_name': 'Province'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modern_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.ModernPrefecture']", 'null': 'True', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'geo.structure': {
            'Meta': {'object_name': 'Structure'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.City']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'japanese_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geo.Province']", 'null': 'True', 'blank': 'True'}),
            'roman_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'y_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'}),
            'z_coordinate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '12', 'blank': 'True'})
        },
        u'people.group': {
            'Meta': {'object_name': 'Group'},
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
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Person']"}),
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
            'Meta': {'ordering': "['japanese_title']", 'object_name': 'Work'},
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