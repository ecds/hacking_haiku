from haiku.apps.texts.models import Work, Verse, Kigo
from haiku.apps.geo.models import Structure, City, Area, Province
from haiku.apps.people.models import Person
from django_date_extensions import fields as ddx
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateWidget, ManyToManyWidget


# Resource classes for export from admin
class WorkResource(resources.ModelResource):

    class Meta:
        model = Work

        
class VerseResource(resources.ModelResource):
    author = fields.Field(column_name='author', attribute='author', widget=ForeignKeyWidget(Person, 'roman_personal_name'))
    work = fields.Field(column_name='work', attribute='work', widget=ForeignKeyWidget(Work, 'english_title'))
    kigo = fields.Field(column_name='kigo', attribute='kigo', widget=ForeignKeyWidget(Kigo, 'japanese'))
    #roman_date = fields.Field(column_name='roman_date', attribute='roman_date', widget=DateWidget('%d/%m/%Y'))
    encounters = fields.Field(column_name='encounters', attribute='encounters', widget=ManyToManyWidget(Person, ',', 'roman_personal_name'))
    structures = fields.Field(column_name='structures', attribute='structures', widget=ManyToManyWidget(Structure, ',', 'roman_name'))
    cities  = fields.Field(column_name='cities', attribute='cities', widget=ManyToManyWidget(City, ',', 'roman_name'))
    provinces = fields.Field(column_name='provinces', attribute='provinces', widget=ManyToManyWidget(Province, ',', 'roman_name'))
    areas = fields.Field(column_name='areas', attribute='areas', widget=ManyToManyWidget(Area, ',', 'roman_name'))
    allusions = fields.Field(column_name='allusions', attribute='allusions', widget=ManyToManyWidget(Work, ',', 'english_title'))
    class Meta:
        model = Verse
        export_order = ('id', 'japanese_text', 'english_text', 'romanization', 'author', 'work', 'other_works', 'japanese_date', 'roman_date', 'kigo', 'genre', 'encounters', 'structures', 'cities', 'provinces', 'areas', 'allusions', 'notes')
        
class KigoResource(resources.ModelResource):

    class Meta:
        model = Kigo
        
