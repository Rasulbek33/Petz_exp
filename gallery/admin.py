from django.contrib import admin
from gallery.models import Gallery

@admin.register(Gallery)
class Gallery(admin.ModelAdmin):
    list_display = ('photo_messege',)
    list_display_links = ('photo_messege',)
    search_fields = ('photo_messege',)
