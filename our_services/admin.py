from django.contrib import admin
from our_services.models import Our_Service, About_petz

@admin.register(Our_Service)
class Our_Service(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'helping',)
    list_display_links = ('title', 'helping',)
    search_fields = ('title',)

@admin.register(About_petz)
class About_petz(admin.ModelAdmin):
    list_display = ('to_do', 'about_petz',)
    list_display_links = ('to_do', 'about_petz',)
    search_fields = ('to_do',)
