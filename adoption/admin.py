from django.contrib import admin
from adoption.models import  Adoption, Adoption_name

@admin.register(Adoption)
class Adoption(admin.ModelAdmin):
    list_display = ('title', 'sub_title','about_title', 'about_sub_title', )
    list_display_links = ('title', 'about_title', )
    search_fields = ('title', 'about_title', )

@admin.register(Adoption_name)
class Adoption_name(admin.ModelAdmin):
    list_display = ('petz_name', 'petz_news',)
    list_display_links = ('petz_name',)
    search_fields = ('petz_name',)

