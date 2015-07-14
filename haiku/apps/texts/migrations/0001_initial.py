# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_date_extensions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '__first__'),
        ('people', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltVerse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('japanese_text', models.TextField()),
                ('english_text', models.TextField(blank=True)),
                ('romanization', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['japanese_text'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kigo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('japanese', models.CharField(max_length=50)),
                ('english', models.CharField(max_length=50)),
                ('romanization', models.CharField(max_length=50)),
                ('season', models.CharField(max_length=10, choices=[(b'Fall', b'Fall'), (b'Spring', b'Spring'), (b'Summer', b'Summer'), (b'Winter', b'Winter')])),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['japanese'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('japanese_text', models.CharField(max_length=255)),
                ('english_text', models.TextField(blank=True)),
                ('romanization', models.TextField(blank=True)),
                ('japanese_date', models.CharField(max_length=255, blank=True)),
                ('roman_date', django_date_extensions.fields.ApproximateDateField(help_text=b'YYYY, MM/YYYY, DD/MM/YYYY<br>Visit <a href="http://keisan.casio.jp/exec/system/1239884730" target="_blank">Keisan website</a> to convert', max_length=10, null=True, blank=True)),
                ('genre', models.CharField(max_length=255, blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['author', 'japanese_text'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('japanese_title', models.CharField(max_length=255, blank=True)),
                ('english_title', models.CharField(max_length=255)),
                ('romanized_title', models.CharField(max_length=255, blank=True)),
                ('japanese_date', models.CharField(max_length=255, blank=True)),
                ('roman_date', django_date_extensions.fields.ApproximateDateField(help_text=b'YYYY, MM/YYYY, DD/MM/YYYY<br>Visit <a href="http://keisan.casio.jp/exec/system/1239884730" target="_blank">Keisan website</a> to convert', max_length=10, null=True, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('authors', models.ManyToManyField(to='people.Person', null=True, verbose_name=b'Author(s)', blank=True)),
            ],
            options={
                'ordering': ['english_title'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='verse',
            name='allusions',
            field=models.ManyToManyField(related_name='allusions', null=True, to='texts.Work', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='verse',
            name='areas',
            field=models.ManyToManyField(help_text=b'Non-province areas such as lakes and mountains<br>', to='geo.Area', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='verse',
            name='author',
            field=models.ForeignKey(blank=True, to='people.Person', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='verse',
            name='cities',
            field=models.ManyToManyField(to='geo.City', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='verse',
            name='encounters',
            field=models.ManyToManyField(related_name='encounters', null=True, to='people.Person', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='verse',
            name='kigo',
            field=models.ForeignKey(blank=True, to='texts.Kigo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='verse',
            name='other_works',
            field=models.ManyToManyField(related_name='other_works', null=True, verbose_name=b'Additional Publications', to='texts.Work', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='verse',
            name='provinces',
            field=models.ManyToManyField(to='geo.Province', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='verse',
            name='structures',
            field=models.ManyToManyField(to='geo.Structure', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='verse',
            name='work',
            field=models.ForeignKey(blank=True, to='texts.Work', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='altverse',
            name='verse',
            field=models.ForeignKey(to='texts.Verse'),
            preserve_default=True,
        ),
    ]
