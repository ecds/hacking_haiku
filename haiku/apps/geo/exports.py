from haiku.apps.geo.models import Province, ModernPrefecture, City, ModernCity, Structure, Area, ModernArea
from import_export import resources


# Resource classes for export
class ProvinceResource(resources.ModelResource):

    class Meta:
        model = Province

        
class ModernPrefectureResource(resources.ModelResource):

    class Meta:
        model = ModernPrefecture

        
class CityResource(resources.ModelResource):

    class Meta:
        model = City

        
class ModernCityResource(resources.ModelResource):

    class Meta:
        model = ModernCity


class AreaResource(resources.ModelResource):

    class Meta:
        model = Area

        
class ModernAreaResource(resources.ModelResource):

    class Meta:
        model = ModernArea

        
class StructureResource(resources.ModelResource):

    class Meta:
        model = Structure
    
