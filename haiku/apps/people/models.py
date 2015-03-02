from django.db import models
from django.utils.safestring import mark_safe 
from import_export import resources
from django_date_extensions import fields as ddx

#Roles
class RoleManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

    
class Role(models.Model):
    '''People roles'''
    
    objects = RoleManager()

    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    def natural_key(self):
        return self.name
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

    
#Groups
class GroupManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

    
class Group(models.Model):
    '''Group of people'''
    
    objects = GroupManager()

    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    def natural_key(self):
        return self.name
    
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
    
    
# Person and person parts
class PersonManager(models.Manager):
    def get_by_natural_key(self, first_name, last_name):
        return self.get(first_name=first_name, last_name=last_name)

    
class Person(models.Model):

    objects = PersonManager()

    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    japanese_family_name = models.CharField(max_length=100, blank=True, verbose_name='Japanese family name')
    japanese_personal_name = models.CharField(max_length=100, blank=True, verbose_name='Japanese personal name(s)')
    roman_family_name = models.CharField(max_length=100, blank=True, verbose_name='Romanized family name')
    roman_personal_name = models.CharField(max_length=100, verbose_name='Romanized personal name(s)')
    birth_japanese = models.CharField(max_length=255, blank=True, verbose_name='Birth, Japanese date')
    death_japanese = models.CharField(max_length=255, blank=True, verbose_name='Death, Japanese date')
    birth_roman = ddx.ApproximateDateField(blank=True, verbose_name='Birth, Roman date', help_text=mark_safe('YYYY, MM/YYYY, DD/MM/YYYY<br>Visit <a href="http://keisan.casio.jp/exec/system/1239884730" target="_blank">Keisan website</a> to convert'))
    death_roman = ddx.ApproximateDateField(blank=True, verbose_name='Death, Roman date', help_text=mark_safe('YYYY, MM/YYYY, DD/MM/YYYY<br>Visit <a href="http://keisan.casio.jp/exec/system/1239884730" target="_blank">Keisan website</a> to convert'))
    gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES)
    roles = models.ManyToManyField('Role', blank=True, null=True)
    groups = models.ManyToManyField('Group', blank=True, null=True)
    uri = models.URLField(blank=True, help_text=mark_safe('<a href="http://www.viaf.org" target="_blank">Virtual International Authority File</a>'))
    notes = models.TextField(blank=True)

    def natural_key(self):
        return (self.roman_family_name, self.roman_personal_name)
    
    def __unicode__(self):
        if not self.roman_family_name:
            return self.roman_personal_name
        else:
            return '%s %s' % (self.roman_family_name, self.roman_personal_name)

    def dates_converted(self):
        if self.birth_japanese != None and self.birth_japanese != '' and \
          self.birth_roman == None or self.birth_roman == '' or \
          self.death_japanese != None and self.death_japanese != '' and \
          self.death_roman == None or self.death_roman == '':             
            return False
        else:
            return True
    dates_converted.boolean = True
    dates_converted.short_description = 'JCal'
        
        
    class Meta:
        verbose_name_plural = 'People'
        unique_together = ('roman_family_name', 'roman_personal_name')
        ordering = ['roman_family_name', 'roman_personal_name']

       
        
class NameManager(models.Manager):
    def get_by_natural_key(self, roman_personal_name, roman_family_name, person):
        self.get(roman_personal_name=roman_personal_name, roman_family_name=roman_family_name)


class Name(models.Model):

    objects = NameManager()

    japanese_family_name = models.CharField(max_length=100, blank=True, verbose_name='Japanese family name')
    japanese_personal_name = models.CharField(max_length=100, blank=True, verbose_name='Japanese personal name(s)')
    roman_family_name = models.CharField(max_length=100, verbose_name='Romanized family name')
    roman_personal_name = models.CharField(max_length=100, blank=True, verbose_name='Romanized personal name(s)')
    person = models.ForeignKey('Person')

    def natural_key(self):
        return (self.roman_family_name, self.roman_personal_name)

    def __unicode__(self):
        if not self.roman_personal_name:
            return self.roman_family_name
        else:
            return '%s %s' % (self.roman_family_name, self.roman_personal_name)


class PenNameManager(models.Manager):
    def get_by_natural_key(self, roman_name):
        return self.get(roman_name=roman_name)


class PenName(models.Model):

    objects = PenNameManager()

    japanese_name = models.CharField(blank=True, max_length=200)
    roman_name = models.CharField(max_length=200, verbose_name='Romanized name')
    person = models.ForeignKey('Person')

    def natural_key(self):
        return (self.romanized_name)

    def __unicode__(self):
        return self.romanized_name

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
