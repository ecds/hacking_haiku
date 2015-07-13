from django.db import models
from import_export import resources


class ModernPrefectureManager(models.Manager):
    def get_by_natural_key(self, roman_name):
        return self.get(roman_name=roman_name)

     
class ModernPrefecture(models.Model):
    '''Name of modern Japanese prefecture'''

    objects = ModernPrefectureManager()

    japanese_name = models.CharField(max_length=255, blank=True)
    roman_name = models.CharField(max_length=255)
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
    roman_name = models.CharField(max_length=255)
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
    roman_name = models.CharField(max_length=255)
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
    roman_name = models.CharField(max_length=255)
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
    roman_name = models.CharField(max_length=255)
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
    roman_name = models.CharField(max_length=255)
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
    roman_name = models.CharField(max_length=255)
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
    

