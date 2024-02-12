from django.db import models

class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery/%Y/%m/%d', help_text='photo')
    photo_messege = models.CharField(max_length=50, help_text='photo_news')



    def __str__(self) -> str:
        return self.photo_messege
    

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallerys'
        
