# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Role'
        db.create_table(u'people_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'people', ['Role'])

        # Adding model 'Group'
        db.create_table(u'people_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'people', ['Group'])

        # Adding model 'Person'
        db.create_table(u'people_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_family_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('japanese_personal_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('roman_family_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('roman_personal_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('birth_japanese', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('death_japanese', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('birth_roman', self.gf('django_date_extensions.fields.ApproximateDateField')(max_length=10, blank=True)),
            ('death_roman', self.gf('django_date_extensions.fields.ApproximateDateField')(max_length=10, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'people', ['Person'])

        # Adding unique constraint on 'Person', fields ['roman_family_name', 'roman_personal_name']
        db.create_unique(u'people_person', ['roman_family_name', 'roman_personal_name'])

        # Adding M2M table for field roles on 'Person'
        m2m_table_name = db.shorten_name(u'people_person_roles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'people.person'], null=False)),
            ('role', models.ForeignKey(orm[u'people.role'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'role_id'])

        # Adding M2M table for field groups on 'Person'
        m2m_table_name = db.shorten_name(u'people_person_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'people.person'], null=False)),
            ('group', models.ForeignKey(orm[u'people.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'group_id'])

        # Adding model 'Name'
        db.create_table(u'people_name', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_family_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('japanese_personal_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('roman_family_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('roman_personal_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
        ))
        db.send_create_signal(u'people', ['Name'])

        # Adding model 'PenName'
        db.create_table(u'people_penname', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('japanese_name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('roman_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'])),
        ))
        db.send_create_signal(u'people', ['PenName'])


    def backwards(self, orm):
        # Removing unique constraint on 'Person', fields ['roman_family_name', 'roman_personal_name']
        db.delete_unique(u'people_person', ['roman_family_name', 'roman_personal_name'])

        # Deleting model 'Role'
        db.delete_table(u'people_role')

        # Deleting model 'Group'
        db.delete_table(u'people_group')

        # Deleting model 'Person'
        db.delete_table(u'people_person')

        # Removing M2M table for field roles on 'Person'
        db.delete_table(db.shorten_name(u'people_person_roles'))

        # Removing M2M table for field groups on 'Person'
        db.delete_table(db.shorten_name(u'people_person_groups'))

        # Deleting model 'Name'
        db.delete_table(u'people_name')

        # Deleting model 'PenName'
        db.delete_table(u'people_penname')


    models = {
        u'people.group': {
            'Meta': {'object_name': 'Group'},
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
            'Meta': {'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['people']