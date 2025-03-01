from django.contrib import admin
from .models import Client, Personnel, Administrateur

# Register your models here.
admin.site.register(Client)
admin.site.register(Personnel)
admin.site.register(Administrateur)