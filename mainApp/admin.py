from django.contrib import admin

# Register your models here.
from mainApp.models import category, customCategory, product

admin.site.register(category)
admin.site.register(customCategory)
admin.site.register(product)
