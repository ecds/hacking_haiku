from haiku.apps.people.models import Group, Person, Role
from import_export import resources, fields
from import_export.widgets import DateWidget, ManyToManyWidget


# Resource classes for export
class RoleResource(resources.ModelResource):

    class Meta:
        model = Role

        
class GroupResource(resources.ModelResource):

    class Meta:
        model = Group

        
class PersonResource(resources.ModelResource):
    roles = fields.Field(column_name='roles', attribute='roles', widget=ManyToManyWidget(Role, ',', 'name'))
    groups = fields.Field(column_name='groups', attribute='groups', widget=ManyToManyWidget(Group, ',', 'name'))

    class Meta:
        model = Person
        export_order = ('japanese_family_name', 'japanese_personal_name', 'roman_family_name', 'roman_personal_name', 'birth_japanese', 'death_japanese', 'birth_roman', 'death_roman', 'gender', 'roles', 'groups', 'uri', 'notes')
