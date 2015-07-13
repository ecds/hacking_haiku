from haiku.apps.geo.models import Province, ModernPrefecture, City, ModernCity, Structure, Area, ModernArea
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget


# Resource classes for export
class ProvinceResource(resources.ModelResource):
    modern_name = fields.Field(column_name='modern_name', attribute='modern_name', widget=ForeignKeyWidget(ModernPrefecture, 'roman_name'))
    
    class Meta:
        model = Province
        export_order = ('japanese_name', 'roman_name', 'modern_name', 'x_coordinate', 'y_coordinate', 'notes')

        
class ModernPrefectureResource(resources.ModelResource):

    class Meta:
        model = ModernPrefecture

        
class CityResource(resources.ModelResource):
    modern_name = fields.Field(column_name='modern_name', attribute='modern_name', widget=ForeignKeyWidget(ModernPrefecture, 'roman_name'))
    province = fields.Field(column_name='province', attribute='province', widget=ForeignKeyWidget(Province, 'roman_name'))
    
    class Meta:
        model = City
        export_order = ('japanese_name', 'roman_name', 'modern_name', 'province', 'x_coordinate', 'y_coordinate', 'notes')

        
class ModernCityResource(resources.ModelResource):
    prefecture = fields.Field(column_name='prefecture', attribute='prefecture', widget=ForeignKeyWidget(ModernPrefecture, 'roman_name'))
    
    class Meta:
        model = ModernCity
        export_order = ('japanese_name', 'roman_name', 'prefecture', 'x_coordinate', 'y_coordinate', 'notes')


class AreaResource(resources.ModelResource):
    modern_name = fields.Field(column_name='modern_name', attribute='modern_name', widget=ForeignKeyWidget(ModernArea, 'roman_name'))
    
    class Meta:
        model = Area
        export_order = ('japanese_name', 'roman_name', 'modern_name', 'x_coordinate', 'y_coordinate', 'notes')

        
class ModernAreaResource(resources.ModelResource):
    
    class Meta:
        model = ModernArea

        
class StructureResource(resources.ModelResource):
    city = fields.Field(column_name='city', attribute='city', widget=ForeignKeyWidget(City, 'roman_name'))
    province = fields.Field(column_name='province', attribute='province', widget=ForeignKeyWidget(Province, 'roman_name'))
    
    class Meta:
        model = Structure
        export_order = ('japanese_name', 'roman_name', 'city', 'province', 'x_coordinate', 'y_coordinate', 'z_coordinate', 'notes')
    
