from django.db import models
from django.utils.safestring import mark_safe 
from django_date_extensions import fields as ddx
from adminsortable.models import Sortable


class ModernPrefectureManager(models.Manager):
    def get_by_natural_key(self, roman_name):
        return self.get(roman_name=roman_name)

     
class ModernPrefecture(models.Model):
    '''Name of modern Japanese prefecture'''

    objects = ModernPrefectureManager()

    japanese_name = models.CharField(max_length=255, blank=True)
    roman_name = models.CharField(max_length=255, unique=True)
    x_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    y_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    notes = models.TextField(blank=True)
    
    # generate natural key
    def natural_key(self):
        return (self.roman_name)

    def __unicode__(self):
        return self.roman_name

    class Meta:
        ordering = ['roman_name']


class ProvinceManager(models.Manager):
     def get_by_natural_key(self, roman_name):
        return self.get(roman_name=roman_name)
     
class Province(models.Model):
    '''Name of 18th/19th century Japanese province'''

    objects = ProvinceManager()

    japanese_name = models.CharField(max_length=255, blank=True)
    roman_name = models.CharField(max_length=255, unique=True)
    modern_name = models.ForeignKey('ModernPrefecture', blank=True, null=True)
    x_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    y_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    notes = models.TextField(blank=True)


    # generate natural key
    def natural_key(self):
        return (self.roman_name)

    def __unicode__(self):
        return self.roman_name

    class Meta:
        ordering = ['roman_name']
        
class ModernCityManager(models.Manager):
    def get_by_natural_key(self, roman_name):
        return self.get(roman_name=roman_name)

     
class ModernCity(models.Model):
    '''Name of modern Japanese city'''

    objects = ModernCityManager()

    japanese_name =  models.CharField(max_length=255, blank=True)
    roman_name = models.CharField(max_length=255, unique=True)
    prefecture = models.ForeignKey('ModernPrefecture', blank=True, null=True)
    x_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    y_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    notes = models.TextField(blank=True)

    # generate natural key
    def natural_key(self):
        return (self.roman_name)

    def __unicode__(self):
        return self.roman_name 

    class Meta:
        verbose_name_plural = 'Modern cities'
        ordering = ['roman_name']
         
    
class CityManager(models.Manager):
     def get_by_natural_key(self, roman_name):
        return self.get(roman_name=roman_name)

     
class City(models.Model):
    '''Name of 18th/19th century Japanese city'''

    objects = CityManager()

    japanese_name =  models.CharField(max_length=255, blank=True)
    roman_name = models.CharField(max_length=255, unique=True)
    modern_name = models.ForeignKey('ModernCity', blank=True, null=True)
    province = models.ForeignKey('Province', blank=True, null=True)
    x_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    y_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    notes = models.TextField(blank=True)

    # generate natural key
    def natural_key(self):
        return (self.roman_name)

    def __unicode__(self):
        return self.roman_name

    class Meta:
        verbose_name_plural = 'Cities'
        ordering = ['roman_name']

        
class ModernAreaManager(models.Manager):
    def get_by_natural_key(self, roman_name):
        return self.get(roman_name=roman_name)

     
class ModernArea(models.Model):
    '''Name of modern Japanese area'''

    objects = ModernAreaManager()

    japanese_name =  models.CharField(max_length=255, blank=True)
    roman_name = models.CharField(max_length=255, unique=True)
    x_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    y_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    notes = models.TextField(blank=True)
    
    # generate natural key
    def natural_key(self):
        return (self.roman_name)

    def __unicode__(self):
        return self.roman_name 

    class Meta:
        verbose_name_plural = 'Modern areas'      
        ordering = ['roman_name']

        
class AreaManager(models.Manager):
     def get_by_natural_key(self, roman_name):
        return self.get(roman_name=roman_name)

     
class Area(models.Model):
    '''Name of 18th/19th century Japanese area'''

    objects = AreaManager()

    japanese_name =  models.CharField(max_length=255, blank=True)
    roman_name = models.CharField(max_length=255, unique=True)
    modern_name = models.ForeignKey('ModernArea', blank=True, null=True)
    x_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    y_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    notes = models.TextField(blank=True)

    # generate natural key
    def natural_key(self):
        return (self.roman_name)

    def __unicode__(self):
        return self.roman_name

    class Meta:
        verbose_name_plural = 'Areas'
        ordering = ['roman_name']

   
class StructureManager(models.Manager):
     def get_by_natural_key(self, roman_name):
        return self.get(roman_name=roman_name)

     
class Structure(models.Model):
    '''Name of 18th/19th century Japanese structure'''

    objects = StructureManager()

    japanese_name =  models.CharField(max_length=255, blank=True)
    roman_name = models.CharField(max_length=255, unique=True)
    city = models.ForeignKey('City', blank=True, null=True)
    province = models.ForeignKey('Province', blank=True, null=True)
    x_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    y_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    z_coordinate = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    notes = models.TextField(blank=True)

    # generate natural key
    def natural_key(self):
        return (self.roman_name)

    def __unicode__(self):
        return self.roman_name

    class Meta:
        ordering = ['roman_name']


class Stop(Sortable):
    objects = models.Manager()

    class Meta(Sortable.Meta):
        pass

    city =  models.ForeignKey('City', blank=True, null=True)
    province =  models.ForeignKey('Province', blank=True, null=True)
    area =  models.ForeignKey('Area', blank=True, null=True)
    structure =  models.ForeignKey('Structure', blank=True, null=True)
    japanese_date = models.CharField(max_length=255, blank=True)
    roman_date = ddx.ApproximateDateField(blank=True, null=True, help_text=mark_safe('YYYY, MM/YYYY, DD/MM/YYYY<br>Visit <a href="http://keisan.casio.jp/exec/system/1239884730" target="_blank">Keisan website</a> to convert'))  
    notes = models.TextField(blank=True)

    def __unicode__(self):
        parts = []
        if self.city:
            parts.append(self.city.roman_name)
        if self.province:
            parts.append(self.province.roman_name)
        if self.area:
            parts.append(self.area.roman_name)
        if self.structure:
            parts.append(self.structure.roman_name)
        if self.roman_date:
            parts.append(str(self.roman_date))
        parts = [x for x in parts if x != None]
        return ' - '.join(parts)


class StopVerse(models.Model):
    objects = models.Manager()

    stop = models.ForeignKey('Stop')
    verse = models.ForeignKey('texts.Verse')
