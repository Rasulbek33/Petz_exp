from django.db import models
from contact.abstract import BaseModel


class Gallery(BaseModel):
    photo = models.ImageField(upload_to='gallery/%Y/%m/%d', help_text='photo')
    photo_messege = models.CharField(max_length=50, help_text='photo_news')



    def __str__(self) -> str:
        return self.photo_messege
    

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallerys'
        
