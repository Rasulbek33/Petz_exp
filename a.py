from django.db import models



class Adoption(models.Model):
    photo = models.ImageField(upload_to='adoption/%Y/%m/%d', help_text='photo', blank=True)
    title = models.CharField(max_length=50, help_text='title', blank=True)
    sub_title = models.TextField(help_text='sub_title', blank=True) 
    about_title = models.CharField(max_length=100, verbose_name='about_title', blank=True)
    about_sub_title = models.CharField(max_length=100, help_text='about_sub_title', blank=True)

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Adoption'
        verbose_name_plural = 'Adoptions'


class Adoption_name(models.Model):
    petz_img = models.ImageField(upload_to='petz_image/%Y/%m/%d', help_text='petz_image')
    petz_name = models.CharField(max_length=30, help_text='petz_name')
    petz_news = models.CharField(max_length=200, help_text='petz_news')

    def __str__(self) -> str:
        return self.petz_name
    
    class Meta:
        verbose_name = 'Adoption_name'
        verbose_name_plural = 'Adoption_names'



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

