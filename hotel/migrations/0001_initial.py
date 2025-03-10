# Generated by Django 5.1.4 on 2025-03-01 11:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utilisateur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChambreHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroChambre', models.PositiveIntegerField(unique=True)),
                ('type', models.CharField(choices=[('Simple', 'Chambre Simple'), ('Double', 'Chambre Double'), ('Suite', 'Suite'), ('Familiale', 'Chambre Familiale'), ('Executive', 'Chambre Executive'), ('Deluxe', 'Chambre Deluxe'), ('Junior Suite', 'Junior Suite'), ('Presidentielle', 'Suite Présidentielle'), ('Chambre avec vue mer', 'Chambre avec vue mer'), ('Chambre avec vue jardin', 'Chambre avec vue jardin'), ('Chambre communicante', 'Chambre communicante'), ('Chambre accessible aux PMR', 'Chambre accessible aux personnes à mobilité réduite')], default='Simple', max_length=50)),
                ('etage', models.PositiveIntegerField()),
                ('prix', models.PositiveIntegerField()),
                ('petit_dejeuner', models.CharField(choices=[('Non', 'Non'), ('Oui', 'Oui')], default='Non')),
                ('disponibilite', models.CharField(choices=[('Non', 'Non'), ('Oui', 'Oui')], default='Oui')),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_chambre/')),
            ],
        ),
        migrations.CreateModel(
            name='Etage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_etage', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('adresse', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_hotel/')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_personnes', models.PositiveIntegerField()),
                ('nombre_nuits', models.PositiveIntegerField()),
                ('petit_dejeuner', models.CharField(choices=[('Non', 'Non'), ('Oui', 'Oui')], default='Non')),
                ('montant', models.PositiveIntegerField(editable=False)),
                ('date_reservation', models.DateTimeField(auto_now_add=True)),
                ('chambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.chambrehotel')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utilisateur.client')),
            ],
        ),
    ]
