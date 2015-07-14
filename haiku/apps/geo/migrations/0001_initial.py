# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_date_extensions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('japanese_name', models.CharField(max_length=255, blank=True)),
                ('roman_name', models.CharField(unique=True, max_length=255)),
                ('x_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('y_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['roman_name'],
                'verbose_name_plural': 'Areas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('japanese_name', models.CharField(max_length=255, blank=True)),
                ('roman_name', models.CharField(unique=True, max_length=255)),
                ('x_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('y_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['roman_name'],
                'verbose_name_plural': 'Cities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModernArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('japanese_name', models.CharField(max_length=255, blank=True)),
                ('roman_name', models.CharField(unique=True, max_length=255)),
                ('x_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('y_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['roman_name'],
                'verbose_name_plural': 'Modern areas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModernCity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('japanese_name', models.CharField(max_length=255, blank=True)),
                ('roman_name', models.CharField(unique=True, max_length=255)),
                ('x_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('y_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['roman_name'],
                'verbose_name_plural': 'Modern cities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModernPrefecture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('japanese_name', models.CharField(max_length=255, blank=True)),
                ('roman_name', models.CharField(unique=True, max_length=255)),
                ('x_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('y_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['roman_name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('japanese_name', models.CharField(max_length=255, blank=True)),
                ('roman_name', models.CharField(unique=True, max_length=255)),
                ('x_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('y_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('modern_name', models.ForeignKey(blank=True, to='geo.ModernPrefecture', null=True)),
            ],
            options={
                'ordering': ['roman_name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(default=1, editable=False, db_index=True)),
                ('japanese_date', models.CharField(max_length=255, blank=True)),
                ('roman_date', django_date_extensions.fields.ApproximateDateField(help_text=b'YYYY, MM/YYYY, DD/MM/YYYY<br>Visit <a href="http://keisan.casio.jp/exec/system/1239884730" target="_blank">Keisan website</a> to convert', max_length=10, null=True, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('area', models.ForeignKey(blank=True, to='geo.Area', null=True)),
                ('city', models.ForeignKey(blank=True, to='geo.City', null=True)),
                ('province', models.ForeignKey(blank=True, to='geo.Province', null=True)),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StopVerse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stop', models.ForeignKey(to='geo.Stop')),
                ('verse', models.ForeignKey(to='texts.Verse')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('japanese_name', models.CharField(max_length=255, blank=True)),
                ('roman_name', models.CharField(unique=True, max_length=255)),
                ('x_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('y_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('z_coordinate', models.DecimalField(null=True, max_digits=15, decimal_places=12, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('city', models.ForeignKey(blank=True, to='geo.City', null=True)),
                ('province', models.ForeignKey(blank=True, to='geo.Province', null=True)),
            ],
            options={
                'ordering': ['roman_name'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='stop',
            name='structure',
            field=models.ForeignKey(blank=True, to='geo.Structure', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='moderncity',
            name='prefecture',
            field=models.ForeignKey(blank=True, to='geo.ModernPrefecture', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='modern_name',
            field=models.ForeignKey(blank=True, to='geo.ModernCity', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(blank=True, to='geo.Province', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='modern_name',
            field=models.ForeignKey(blank=True, to='geo.ModernArea', null=True),
            preserve_default=True,
        ),
    ]
