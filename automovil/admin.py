from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Auto, Marca, Modelo

# Register your models here.

class AutoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class MarcaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class ModeloAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Auto, AutoAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Modelo, ModeloAdmin)