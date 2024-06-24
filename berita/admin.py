from django.contrib import admin
from berita.models import kategori, Artikel
# Register your models here.

admin.site.register(kategori)
class ArtikelAdmin(admin.ModelAdmin):
    list_display= ['judul','kategori', 'author']
    search_fields = ['judul']
admin.site.register(Artikel, ArtikelAdmin)