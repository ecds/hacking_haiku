from haiku.apps.admin.models import LinkedInline, get_admin_url
from haiku.apps.texts.models import Work, Verse, Kigo
from haiku.apps.people.forms import PersonForm, GroupForm
from haiku.apps.people.models import Group, Person, Name, PenName, Role, RoleResource, GroupResource, PersonResource
from django.conf import settings
from django.contrib import admin
from import_export.admin import ExportActionModelAdmin


class PeopleInline(admin.TabularInline):
    model = Person.groups.through
    verbose_name = 'Person'
    verbose_name_plural = 'People'
    extra = 1

    
class RoleExport(ExportActionModelAdmin):
    resource_class = RoleResource
    to_encoding = 'utf-8'
    pass


class RoleAdmin(RoleExport, admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
admin.site.register(Role, RoleAdmin)


class GroupExport(ExportActionModelAdmin):
    resource_class = GroupResource
    to_encoding = 'utf-8'
    pass


class GroupAdmin(GroupExport, admin.ModelAdmin):
    form = GroupForm
    list_display = ['name']
    search_fields = ['name']
    inlines = [
        PeopleInline,
    ]
    
admin.site.register(Group, GroupAdmin)


class AltNamesInline(admin.TabularInline):
    model = Name
    verbose_name_plural = 'Alternate Names'
    extra = 1

    
class PenNamesInline(admin.TabularInline):
    model = PenName
    verbose_name_plural = 'Pen Names'
    extra = 1

    
class PersonExport(ExportActionModelAdmin):
    resource_class = PersonResource
    to_encoding = 'utf-8'
    pass


class PersonAdmin(PersonExport, admin.ModelAdmin):
    class Media:
      js = (settings.STATIC_URL + 'js/admin/collapseTabularInlines.js',)
      css = { "all" : (settings.STATIC_URL +"css/admin/admin_styles.css",) }
    list_display = ['roman_family_name', 'roman_personal_name', 'gender', 'uri', 'dates_converted']
    list_filter = ['gender', 'groups', 'roles']
    search_fields = ['roman_family_name', 'roman_personal_name', 'gender', 'notes', 'uri']
    list_display_links = ['roman_family_name', 'roman_personal_name']
    inlines = [
        AltNamesInline,
        PenNamesInline,
    ]
    form = PersonForm

admin.site.register(Person, PersonAdmin)
