# tienda/admin.py
from django.contrib import admin
from .models import Product

# Define admin actions here

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )  # Campo created como solo lectura

# Registrar el modelo Product y el admin personalizado
admin.site.register(Product, ProductAdmin)
