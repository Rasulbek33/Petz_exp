from django.contrib import admin
from our_team.models import Our_team, Author

@admin.register(Our_team)
class Our_team(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'author',)
    list_display_links = ('title', 'sub_title',)
    search_fields = ('title',)

@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ('author', 'job', 'author_about', 'admin_photo',)
    list_display_links = ('author', 'job',)
    search_fields = ('author', 'admin_photo',)
