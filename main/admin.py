from django.contrib import admin
from main.models import  Home


@admin.register(Home)
class Home(admin.ModelAdmin):
    list_display = ("title", 'sub_title', 'about_title', 'about_sub_title',)
    list_display_links = ("title", 'sub_title','about_title',)
    search_fields = ("title", 'sub_title', 'about_title')
    # list_filter = ("created_at",)