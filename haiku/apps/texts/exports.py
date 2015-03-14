from haiku.apps.texts.models import Work, Verse, Kigo
from import_export import resources


# Resource classes for export
class WorkResource(resources.ModelResource):

    class Meta:
        model = Work

        
class VerseResource(resources.ModelResource):
    #author = fields.Field(column_name='author', attribute='author', widget=ForeignKeyWidget(Person, 'name'))
    #work
    #kigo
    class Meta:
        model = Verse

        
class KigoResource(resources.ModelResource):

    class Meta:
        model = Kigo
        
