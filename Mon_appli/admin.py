from django.contrib import admin
from .models import Candidat

@admin.register(Candidat)
class CandidatAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'telephone', 'date_inscription')
    list_filter = ('date_inscription',)
    search_fields = ('nom', 'prenom', 'email')
    readonly_fields = ('date_inscription',)