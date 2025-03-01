from django.contrib import admin
from .models import Hotel, Etage, ChambreHotel, Reservation


class HotelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'telephone', 'email', 'description', 'image')
    list_filter = ('nom', 'adresse', 'telephone', 'email', 'description', 'image')
    search_fields = ('nom', 'adresse', 'telephone', 'email', 'description', 'image')
    list_per_page = 10

admin.site.register(Hotel, HotelAdmin)

class EtageAdmin(admin.ModelAdmin):
    list_display = ('numero_etage',)
    list_filter = ('numero_etage',)
    search_fields = ('numero_etage',)
    list_per_page = 10

admin.site.register(Etage, EtageAdmin)

class ChambreHotelAdmin(admin.ModelAdmin):
    list_display = ('numeroChambre', 'type', 'etage', 'prix', 'petit_dejeuner', 'disponibilite', 'description', 'image')
    list_filter = ('type', 'etage', 'prix', 'petit_dejeuner', 'disponibilite', 'description', 'image')
    search_fields = ('numeroChambre', 'type', 'etage', 'prix', 'petit_dejeuner', 'disponibilite', 'description', 'image')
    list_per_page = 10

admin.site.register(ChambreHotel, ChambreHotelAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('client', 'chambre', 'nombre_personnes', 'nombre_nuits', 'petit_dejeuner', 'montant', 'date_reservation')
    list_filter = ('client', 'chambre', 'nombre_personnes', 'nombre_nuits', 'petit_dejeuner', 'montant', 'date_reservation')
    search_fields = ('client', 'chambre', 'nombre_personnes', 'nombre_nuits', 'petit_dejeuner', 'montant', 'date_reservation')
    list_per_page = 10

admin.site.register(Reservation, ReservationAdmin)

