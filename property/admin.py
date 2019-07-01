from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):

    list_display = ('street', 'city', 'state', 'zip_code', 'price', 'bedrooms', 'bathrooms', 'garage', 'square_feet', 'lot_size', 'created_at', )

    list_filter = ['price','city','state','street']
# Register your models here.

admin.site.register(Property, PropertyAdmin)