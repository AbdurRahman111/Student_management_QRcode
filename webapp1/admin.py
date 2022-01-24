from django.contrib import admin
from .models import Verifica_Risultati_Candidato, Esami_sostenuti_e_relativi_esiti
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('MATRICOLA', 'COGNOME', 'NOME', 'DATA_DI_NASCITA', 'NAZIONALITA')
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


class show_Sessione(admin.ModelAdmin):
    list_display = ['Student', 'Sessione', 'Data', 'Esame', 'Centro', 'Parte', 'Esito']

admin.site.register(Verifica_Risultati_Candidato, PostAdmin)
admin.site.register(Esami_sostenuti_e_relativi_esiti, show_Sessione)