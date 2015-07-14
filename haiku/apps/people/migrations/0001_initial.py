# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_date_extensions.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('japanese_family_name', models.CharField(max_length=100, verbose_name=b'Japanese family name', blank=True)),
                ('japanese_personal_name', models.CharField(max_length=100, verbose_name=b'Japanese personal name(s)', blank=True)),
                ('roman_family_name', models.CharField(max_length=100, verbose_name=b'Romanized family name')),
                ('roman_personal_name', models.CharField(max_length=100, verbose_name=b'Romanized personal name(s)', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PenName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('japanese_name', models.CharField(max_length=200, blank=True)),
                ('roman_name', models.CharField(max_length=200, verbose_name=b'Romanized name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('japanese_family_name', models.CharField(max_length=100, verbose_name=b'Japanese family name', blank=True)),
                ('japanese_personal_name', models.CharField(max_length=100, verbose_name=b'Japanese personal name(s)', blank=True)),
                ('roman_family_name', models.CharField(max_length=100, verbose_name=b'Romanized family name', blank=True)),
                ('roman_personal_name', models.CharField(max_length=100, verbose_name=b'Romanized personal name(s)')),
                ('birth_japanese', models.CharField(max_length=255, verbose_name=b'Birth, Japanese date', blank=True)),
                ('death_japanese', models.CharField(max_length=255, verbose_name=b'Death, Japanese date', blank=True)),
                ('birth_roman', django_date_extensions.fields.ApproximateDateField(help_text=b'YYYY, MM/YYYY, DD/MM/YYYY<br>Visit <a href="http://keisan.casio.jp/exec/system/1239884730" target="_blank">Keisan website</a> to convert', max_length=10, verbose_name=b'Birth, Roman date', blank=True)),
                ('death_roman', django_date_extensions.fields.ApproximateDateField(help_text=b'YYYY, MM/YYYY, DD/MM/YYYY<br>Visit <a href="http://keisan.casio.jp/exec/system/1239884730" target="_blank">Keisan website</a> to convert', max_length=10, verbose_name=b'Death, Roman date', blank=True)),
                ('gender', models.CharField(blank=True, max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('uri', models.URLField(help_text=b'<a href="http://www.viaf.org" target="_blank">Virtual International Authority File</a>', blank=True)),
                ('notes', models.TextField(blank=True)),
                ('groups', models.ManyToManyField(to='people.Group', null=True, blank=True)),
            ],
            options={
                'ordering': ['roman_family_name', 'roman_personal_name'],
                'verbose_name_plural': 'People',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='roles',
            field=models.ManyToManyField(to='people.Role', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('roman_family_name', 'roman_personal_name')]),
        ),
        migrations.AddField(
            model_name='penname',
            name='person',
            field=models.ForeignKey(to='people.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='name',
            name='person',
            field=models.ForeignKey(to='people.Person'),
            preserve_default=True,
        ),
    ]
