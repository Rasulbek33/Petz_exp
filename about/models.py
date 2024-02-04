from django.db import models
from contact.abstract import BaseModel


class About(models.Model):
    title = models.CharField(max_length=150, help_text='messege')
    sub_title = models.TextField(max_length=300, help_text='sub_title')
    photo = models.ImageField(upload_to='about/%Y/%m/%d', help_text='photo')
    logo = models.ImageField(upload_to='about/help_service/%Y/%m/%d', help_text='logo')
    logo_title = models.CharField(max_length=50, help_text='logo_title')
    logo_sub_title = models.CharField(max_length=255, help_text='logo_sub_title')


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'




