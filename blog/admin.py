from django.contrib import admin
from blog.models import  Blog

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('photo_title','photo_sub_title', 'news', 'text','created_at',)
    list_display_links = ('photo_title', 'photo_sub_title', 'text')
    search_fields = ('photo_title',)
    list_filter = ("created_at",)
