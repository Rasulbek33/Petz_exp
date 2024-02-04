from django.contrib import admin
from about.models import  About

@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('title', 'sub_title','logo_title', 'logo_sub_title')
    list_display_links = ('title', 'logo_title',)
    search_fields = ('title', 'logo_title',)

