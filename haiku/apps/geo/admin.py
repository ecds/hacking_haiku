from django.contrib import admin
from django.conf import settings
from django.utils.safestring import mark_safe 
from haiku.apps.geo.models import Province, ModernPrefecture, City, ModernCity, Structure, ProvinceResource, ModernPrefectureResource, CityResource, ModernCityResource, StructureResource
from haiku.apps.people.models import Group, Person
from haiku.apps.texts.models import Work, Verse, Kigo
from haiku.apps.admin.models import LinkedInline, get_admin_url
from import_export.admin import ExportActionModelAdmin


class VerseStructureInline(LinkedInline):
    model = Verse.structures.through
    extra = 0
    admin_model_parent = "texts"
    admin_model_path = "verse"
    verbose_name_plural = "Related Verses"

    
class VerseCityInline(LinkedInline):
    model = Verse.cities.through
    extra = 0
    admin_model_parent = "texts"
    admin_model_path = "verse"
    verbose_name_plural = "Related Verses"
  

class ProvinceExport(ExportActionModelAdmin):
    resource_class = ProvinceResource
    to_encoding = 'utf-8'
    pass


class ProvinceAdmin(ProvinceExport, admin.ModelAdmin):
    class Media:
      js = (settings.STATIC_URL + 'js/admin/collapseTabularInlines.js',)
      css = { "all" : (settings.STATIC_URL +"css/admin/admin_styles.css",) }
    list_display = ['name', 'modern_name']
    search_fields = ['name', 'modern_name']
    inlines = [
        
        ]

admin.site.register(Province, ProvinceAdmin)


class ModernPrefectureExport(ExportActionModelAdmin):
    resource_class = ModernPrefecture
    to_encoding = 'utf-8'
    pass


class ModernPrefectureAdmin(ModernPrefectureExport, admin.ModelAdmin):
    class Media:
      js = (settings.STATIC_URL + 'js/admin/collapseTabularInlines.js',)
      css = { "all" : (settings.STATIC_URL +"css/admin/admin_styles.css",) }
    list_display = ['name']
    search_fields = ['name']
    inlines = [
        
        ]

admin.site.register(ModernPrefecture, ModernPrefectureAdmin)


class CityExport(ExportActionModelAdmin):
    resource_class = City
    to_encoding = 'utf-8'
    pass


class CityAdmin(CityExport, admin.ModelAdmin):
    class Media:
      js = (settings.STATIC_URL + 'js/admin/collapseTabularInlines.js',)
      css = { "all" : (settings.STATIC_URL +"css/admin/admin_styles.css",) }
    list_display = ['name', 'province', 'modern_name']
    search_fields = ['name', 'province', 'modern_name']
    inlines = [
        VerseCityInline
        ]

admin.site.register(City, CityAdmin)


class ModernCityExport(ExportActionModelAdmin):
    resource_class = ModernCity
    to_encoding = 'utf-8'
    pass


class ModernCityAdmin(ModernCityExport, admin.ModelAdmin):
    class Media:
      js = (settings.STATIC_URL + 'js/admin/collapseTabularInlines.js',)
      css = { "all" : (settings.STATIC_URL +"css/admin/admin_styles.css",) }
    list_display = ['name', 'prefecture']
    search_fields = ['name', 'prefecture']
    inlines = [
        
        ]

admin.site.register(ModernCity, ModernCityAdmin)


class StructureExport(ExportActionModelAdmin):
    resource_class = Structure
    to_encoding = 'utf-8'
    pass


class StructureAdmin(StructureExport, admin.ModelAdmin):
    class Media:
      js = (settings.STATIC_URL + 'js/admin/collapseTabularInlines.js',)
      css = { "all" : (settings.STATIC_URL +"css/admin/admin_styles.css",) }
    list_display = ['name', 'city', 'province']
    search_fields = ['name', 'city', 'province']
    inlines = [
        VerseStructureInline
        ]

admin.site.register(Structure, StructureAdmin)
