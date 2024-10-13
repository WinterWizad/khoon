from django.contrib import admin


# Register your models here.

from .models import Emergencies


@admin.register(Emergencies)  #It registers with additional features like displays also
class EmergenciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'hospital','age','blood')
    search_fields = ('name', 'hospital','age','blood')

# admin.site.register()   
#It registers
