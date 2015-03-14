from haiku.apps.people.models import Group, Person, Role
from import_export import resources


# Resource classes for export
class RoleResource(resources.ModelResource):

    class Meta:
        model = Role

        
class GroupResource(resources.ModelResource):

    class Meta:
        model = Group

        
class PersonResource(resources.ModelResource):

    class Meta:
        model = Person
