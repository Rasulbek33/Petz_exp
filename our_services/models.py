from django.db import models
from contact.abstract import BaseModel


class Our_Service(BaseModel):
    title = models.CharField(max_length=100, help_text='title')
    sub_title = models.CharField(max_length=255, help_text='sub_title')
    helping = models.CharField(max_length=100, help_text='helping', blank=True)
    photo = models.ImageField(upload_to='our_services/%Y/%m/%d', help_text='photo')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Our_service'
        verbose_name_plural = 'Our_services'


class About_petz(models.Model):
    img = models.ImageField(upload_to='Our_services_about', help_text='image')
    to_do = models.CharField(max_length=50, help_text='qilayotgan ish') 
    about_petz = models.CharField(max_length=100, help_text='hayvon haqida malumot')


    def __str__(self) -> str:
        return self.to_do
    
    class Meta:
        verbose_name = 'About_petz'
        verbose_name_plural = 'About_petzs'
