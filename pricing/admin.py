from django.contrib import admin
from pricing.models import Our_plans, Pricing

@admin.register(Our_plans)
class Our_team(admin.ModelAdmin):
    list_display = ('title', 'sub_title',)
    list_display_links = ('title', )
    search_fields = ('title',)

@admin.register(Pricing)
class Author(admin.ModelAdmin):
    list_display = ('direction', 'price', 'species',)
    list_display_links = ('direction', 'price',)
    search_fields = ('direction',)
