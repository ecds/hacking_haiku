from django.contrib import admin
from django.conf import settings
from haiku.apps.texts.models import Work, Verse, Kigo, WorkResource, VerseResource, KigoResource
from haiku.apps.texts.forms import WorkForm, VerseForm, KigoForm
from haiku.apps.admin.models import LinkedInline, get_admin_url
from import_export.admin import ExportActionModelAdmin


class VerseInline(LinkedInline):
    model = Verse
    extra = 0
    fields = ['japanese_text', 'author']
    readonly_fields = ['japanese_text', 'author']
    verbose_name_plural = "Related Verses"
    admin_model_parent = "texts"
    admin_model_path = "verse"


class WorkExport(ExportActionModelAdmin):
    resource_class = WorkResource
    to_encoding = 'utf-8'
    pass


class WorkAdmin(WorkExport, admin.ModelAdmin):
    class Media:
      js = (settings.STATIC_URL + 'js/admin/collapseTabularInlines.js',)
      css = { "all" : (settings.STATIC_URL +"css/admin/admin_styles.css",) }
    list_display = ['japanese_title', 'english_title', 'romanized_title', 'roman_date', 'dates_converted']
    search_fields = ['japanese_title', 'english_title', 'romanized_title', 'notes']
    form = WorkForm
    inlines = [
        VerseInline,
        ]
admin.site.register(Work, WorkAdmin)

    
class VerseExport(ExportActionModelAdmin):
    resource_class = VerseResource
    to_encoding = 'utf-8'
    pass


class VerseAdmin(VerseExport, admin.ModelAdmin):
    class Media:
      js = (settings.STATIC_URL + 'js/admin/collapseTabularInlines.js',)
      css = { "all" : (settings.STATIC_URL +"css/admin/admin_styles.css",) }
    form = VerseForm
    list_display = ['japanese_text', 'author', 'roman_date', 'kigo', 'dates_converted']
    search_fields = ['japanese_text', 'english_text', 'romanization', 'notes']
    inlines = [
        
    ]
admin.site.register(Verse, VerseAdmin)


class KigoExport(ExportActionModelAdmin):
    resource_class = KigoResource
    to_encoding = 'utf-8'
    form = KigoForm
    pass


class KigoAdmin(KigoExport, admin.ModelAdmin):
    class Media:
      js = (settings.STATIC_URL + 'js/admin/collapseTabularInlines.js',)
      css = { "all" : (settings.STATIC_URL +"css/admin/admin_styles.css",) }
    list_display = ['japanese', 'english', 'romanization', 'season']
    list_filter = ['season']
    search_fields = ['japanese', 'english', 'romanization']
    inlines = [
        VerseInline,
        ]
admin.site.register(Kigo, KigoAdmin)

