from django.db import models
from contact.abstract import BaseModel

class Blog(BaseModel):
    photo = models.ImageField(upload_to='Blog/%Y/%m/%d', help_text='image')
    photo_title = models.CharField(max_length=100, help_text='photo_title')
    photo_sub_title = models.CharField(max_length=255, help_text='photo_sub_title')


    def __str__(self) -> str:
        return self.photo_title
    

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class Lates_posts(BaseModel):
    photo = models.ImageField(upload_to='blog/%Y/%m/%d', help_text='photo')
    news =  models.CharField(max_length=30, help_text='messege')

    def __str__(self) -> str:
        return f"{self.news[:15]}..."
    

    class Meta:
        verbose_name = 'Lates_post'
        verbose_name_plural = 'Lates_posts'


class  About_us(models.Model):
    text = models.CharField(max_length=50, help_text='text')


    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = 'About_us'
        verbose_name_plural = 'Abouts_us'


class Author(BaseModel):
    author = models.CharField(max_length=30, help_text='name')


    def __str__(self) -> str:
        return self.author
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'