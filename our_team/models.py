from django.db import models
from contact.abstract import BaseModel
from django.utils.safestring import mark_safe



class Our_team(BaseModel):
    title = models.CharField(max_length=255, help_text='title')
    sub_title = models.CharField(max_length=255, help_text='sub_title')
    author = models.ForeignKey("Author", on_delete=models.RESTRICT, help_text='author')


    def __str__(self) -> str:
        return self.title


class Author(BaseModel):
    author = models.CharField(max_length=200, help_text='author')
    job = models.CharField(max_length=200, help_text='job')
    image = models.ImageField(upload_to='Our_team/%Y/%m/%d', help_text='author_photo')
    author_about = models.CharField(max_length=255, help_text='author_about')

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />' .format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True


    def __str__(self) -> str:
        return self.author
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'