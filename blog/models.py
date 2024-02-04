from django.db import models
from contact.abstract import BaseModel

class Blog(BaseModel):
    photo = models.ImageField(upload_to='Blog/%Y/%m/%d', help_text='image')
    photo_title = models.CharField(max_length=100, help_text='photo_title')
    photo_sub_title = models.CharField(max_length=255, help_text='photo_sub_title')
    author = models.CharField(max_length=30, help_text='author')
    lates_photo = models.ImageField(upload_to='blog/%Y/%m/%d', help_text='photo', blank=True)
    news =  models.CharField(max_length=30, help_text='messege', blank=True)
    text = models.CharField(max_length=50, help_text='text', blank=True)
    


    def __str__(self) -> str:
        return self.photo_title
    

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'




