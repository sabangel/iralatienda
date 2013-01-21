import main.models as m
from django.contrib import admin

admin.site.register(m.Partners)
admin.site.register(m.Contacts)
admin.site.register(m.Brands)
admin.site.register(m.Types)
admin.site.register(m.Subtypes)
admin.site.register(m.Countries)

class StoresAdmin(admin.ModelAdmin):
    list_display  = ('name', )
admin.site.register(m.Stores, StoresAdmin)

admin.site.register(m.Departments)
admin.site.register(m.Cities)
admin.site.register(m.Neighborhoods)
admin.site.register(m.Delivery_zones)
admin.site.register(m.Products)
admin.site.register(m.Stocks)
admin.site.register(m.Users)
admin.site.register(m.Orders)
admin.site.register(m.Details)
