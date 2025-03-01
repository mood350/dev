from django.contrib import admin
from .models import Client, Personnel, Administrateur

# Register your models here.


class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenoms', 'telephone', 'email', 'fonction', 'date_embauche', 'salaire')
    list_filter = ('fonction', 'date_embauche')
    search_fields = ('nom', 'prenoms', 'telephone', 'email')
    list_per_page = 10

admin.site.register(Personnel, PersonnelAdmin)

class AdministrateurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenoms', 'telephone', 'email', 'fonction', 'date_embauche', 'salaire')
    list_filter = ('fonction', 'date_embauche')
    search_fields = ('nom', 'prenoms', 'telephone', 'email')
    list_per_page = 10

admin.site.register(Administrateur, AdministrateurAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenoms', 'telephone', 'email')
    list_filter = ('nom', 'prenoms', 'telephone', 'email')
    search_fields = ('nom', 'prenoms', 'telephone', 'email')
    list_per_page = 10

admin.site.register(Client, ClientAdmin)
