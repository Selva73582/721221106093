from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.catrgories)

admin.site.register(models.CompanyName)
admin.site.register(models.Product)