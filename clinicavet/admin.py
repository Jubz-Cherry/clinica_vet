from django.contrib import admin
from clinicavet.models import Cliente, Animal, Appoints


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'telephone')
    list_display_links = ('id', 'name')
    list_per_page = 20
    search_fields = ('name', 'telephone')


admin.site.register(Cliente, ClienteAdmin)


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal_name', 'race', 'age', 'cliente')
    list_display_links = ('id', 'animal_name')
    list_per_page = 20
    search_fields = ('animal_name', 'race', 'cliente__name')


admin.site.register(Animal, AnimalAdmin)


class AppointsAdmin(admin.ModelAdmin):
    list_display = ('id', 'animal', 'date', 'hour', 'description')
    list_display_links = ('id', 'animal')
    list_per_page = 20
    search_fields = ('animal__animal_name', 'description')


admin.site.register(Appoints, AppointsAdmin)