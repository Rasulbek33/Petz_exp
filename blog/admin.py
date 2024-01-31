from django.contrib import admin
from blog.models import  Blog, Author, Lates_posts, About_us

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('photo_title','photo_sub_title','created_at',)
    list_display_links = ('photo_title',)
    search_fields = ('photo_title',)
    list_filter = ("created_at",)
    
@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ('author',)
    list_display_links = ('author',)

@admin.register(Lates_posts)
class Lates_post(admin.ModelAdmin):
    list_display = ('news', 'photo', 'created_at',)
    list_display_links = ('news',)

@admin.register(About_us)
class About_us(admin.ModelAdmin):
    list_display = ('text',)
    list_display_links = ('text',)