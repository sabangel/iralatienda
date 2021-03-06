# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

TYPESID = (
	('CC', 'Cédula de ciudadanía'),
	('CD', 'Carnet diplomático'),
	('CE', 'Cédula de extrangería'),
	('NI', 'NIT'),
	('PA', 'Pasaporte'),
)

# Create your models here.
class Contacts(models.Model):
    def __unicode__(self):
        return self.first_name + " " + self.last_name        
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dent_type = models.CharField(max_length=2, choices=TYPESID,  blank = True)
    ident_number = models.CharField(max_length=15,  blank = True)
    phone_number = models.CharField(max_length=12)
    mobile_number = models.CharField(max_length=12,  blank = True)
    email = models.EmailField(max_length=75,  blank = True)
    address = models.CharField(max_length=60,  blank = True)

class Brands(models.Model):
    def __unicode__(self):
        return self.description
    contact = models.ForeignKey(Contacts,  blank = True,  null = True)
    description = models.CharField(max_length=60)
    short_name = models.CharField(max_length=30)

class Types(models.Model):    
    def __unicode__(self):
        return self.description
    description = models.CharField(max_length=100)

class Subtypes(models.Model):    
    def __unicode__(self):
        return self.description
    type = models.ForeignKey(Types)
    description = models.CharField(max_length=100)
    
class Partners(models.Model):    
    def __unicode__(self):
       return self.first_name + " " + self.last_name
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ident_type = models.CharField(max_length=2, choices=TYPESID,  blank = True)
    ident_number = models.CharField(max_length=15,  blank = True)
    phone_number = models.CharField(max_length=12)
    mobile_number = models.CharField(max_length=12,  blank = True)
    email = models.EmailField(max_length=75,  blank = True)
    address = models.CharField(max_length=60,  blank = True)

class Stores(models.Model):    
    def __unicode__(self):
        return self.name        
    partner = models.ForeignKey(Partners)
    nit = models.CharField(max_length=15,  blank = True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=60)
    email = models.EmailField(max_length=75)
    phone_number = models.CharField(max_length=12)
    fax_number = models.CharField(max_length=12,  blank = True)
    fax_enabled = models.BooleanField(default = False)
    min_value = models.FloatField(default = 0)
    is_enabled = models.BooleanField(default = True)
    store_date = models.DateTimeField()    
    
class Images(models.Model):    
    def __unicode__(self):
        return self.name
    store = models.ForeignKey(Stores)
    image = models.ImageField(upload_to="images/stores",  blank = True) 

class Countries(models.Model):    
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=40)

class Departments(models.Model):    
    def __unicode__(self):
        return self.name
    country = models.ForeignKey(Countries)
    name = models.CharField(max_length=40)

class Cities(models.Model):    
    def __unicode__(self):
        return self.name
    department = models.ForeignKey(Departments)
    name = models.CharField(max_length=40)

class Neighborhoods(models.Model):    
    def __unicode__(self):
        return self.name
    city = models.ForeignKey(Cities)
    name = models.CharField(max_length=20)

class Delivery_zones(models.Model):
    store = models.ForeignKey(Stores)
    neigh = models.ForeignKey(Neighborhoods)
    is_home = models.BooleanField(default = False)
    class Meta:
        unique_together = (("store", "neigh"), )

class  Products (models.Model): 
    def __unicode__(self):
        return self.name
    brand = models.ForeignKey(Brands)
    subtype = models.ForeignKey(Subtypes)
    name = models.CharField(max_length=150)
    ref_price = models.FloatField(default = 0)
    image = models.ImageField(upload_to="images/products",  blank = True) 

class Stocks(models.Model):
    store = models.ForeignKey(Stores)
    product = models.ForeignKey(Products)
    exists = models.BooleanField(default = False)
    discount = models.FloatField(default = 0)
    iva = models.FloatField(default = 0)
    price = models.FloatField(default = 0)
    stock_date = models.DateTimeField()
    class Meta():
        unique_together = ("store", "product")
        
class Hist_stocks(models.Model):
    store = models.ForeignKey(Stores)
    product = models.ForeignKey(Products)
    exists = models.BooleanField(default = False)
    discount = models.FloatField(default = 0)
    iva = models.FloatField(default = 0)
    price = models.FloatField(default = 0)
    hist_date = models.DateTimeField()
    class Meta():
        unique_together = ("store", "product")

class Orders(models.Model):
    def __unicode__(self):
        return str(self.user) + " " + str(self.store)
    user = models.ForeignKey(User)
    store = models.ForeignKey(Stores)
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=12)
    subtotal = models.FloatField(default = 0)
    iva = models.FloatField(default = 0)
    discount = models.FloatField(default = 0)
    total = models.FloatField(default = 0)
    order_date = models.DateTimeField()
    is_saved = models.BooleanField(default = False)
    
class Details(models.Model):
    order = models.ForeignKey(Orders)
    product = models.ForeignKey(Products)
    amount = models.IntegerField()
    discount = models.FloatField(default = 0)
    iva = models.FloatField(default = 0)
    sale_price = models.FloatField(default = 0)
    class Meta():
        unique_together = ("order", "product")
