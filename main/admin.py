import main.models as m
from django.contrib import admin

class BrandsAdmin(admin.ModelAdmin):
    list_display  = ('id','contact','description','short_name', )
admin.site.register(m.Brands, BrandsAdmin)

class CitiesAdmin(admin.ModelAdmin):
    list_display  = ('id','department','name',)
admin.site.register(m.Cities,  CitiesAdmin)

class ContactsAdmin(admin.ModelAdmin):
    list_display  = ('id','first_name','last_name','dent_type','ident_number', 
                            'phone_number', 'mobile_number', 'email', 'address' )
admin.site.register(m.Contacts,  ContactsAdmin)

class CountriesAdmin(admin.ModelAdmin):
    list_display  = ('id','name',)
admin.site.register(m.Countries,  CountriesAdmin)

class Delivery_zonesAdmin(admin.ModelAdmin):
    list_display  = ('id','store','neigh','is_home', )
admin.site.register(m.Delivery_zones,  Delivery_zonesAdmin)

class DepartmentsAdmin(admin.ModelAdmin):
    list_display  = ('id','country','name', )
admin.site.register(m.Departments,  DepartmentsAdmin)

class DetailsAdmin(admin.ModelAdmin):
    list_display  = ('id','order','product','amount', 'discount', 'iva', 'sale_price',  )    
admin.site.register(m.Details,  DetailsAdmin)

class Hist_stocksAdmin(admin.ModelAdmin):
    list_display  = ('id','store', 'product', 'exists', 'discount', 'iva', 'price','hist_date', )
admin.site.register(m.Hist_stocks, Hist_stocksAdmin)

class ImagesAdmin(admin.ModelAdmin):
    list_display  = ('id','store', 'image',)
admin.site.register(m.Images, ImagesAdmin)

class NeighborhoodsAdmin(admin.ModelAdmin):
    list_display  = ('id','city','name', )    
admin.site.register(m.Neighborhoods,  NeighborhoodsAdmin)

class OrdersAdmin(admin.ModelAdmin):
    list_display  = ('id','user','store','name','address','phone_number','subtotal', 'iva', 'discount', 'total','order_date', 'is_saved', )     
admin.site.register(m.Orders, OrdersAdmin)

class PartnersAdmin(admin.ModelAdmin):
    list_display  = ('id','first_name', 'last_name', 'ident_type', 'ident_number', 
                            'phone_number', 'mobile_number', 'email', 'address')
admin.site.register(m.Partners, PartnersAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display  = ('id','brand', 'subtype', 'name', 'ref_price', 'image', )
admin.site.register(m.Products, ProductsAdmin)

class StocksAdmin(admin.ModelAdmin):
    list_display  = ('id','store', 'product', 'exists', 'discount', 'iva', 'price','stock_date',  )
admin.site.register(m.Stocks, StocksAdmin)

class StoresAdmin(admin.ModelAdmin):
    list_display  = ('id','partner','nit','name', 'address', 'email', 'phone_number', 'fax_number', 
                    'fax_enabled', 'min_value', 'is_enabled','store_date', )
admin.site.register(m.Stores, StoresAdmin)

class SubtypesAdmin(admin.ModelAdmin):
    list_display  = ('id','type', 'description', )
admin.site.register(m.Subtypes, SubtypesAdmin)

class TypesAdmin(admin.ModelAdmin):
    list_display  = ('id','description', )
admin.site.register(m.Types, TypesAdmin)


