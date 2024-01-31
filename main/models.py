from django.db import models
from django.utils.translation import gettext_lazy as _
from contact.abstract import BaseModel
from ckeditor.fields import RichTextField


class Home(BaseModel):
    title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='Home/image')
    sub_title = models.CharField(max_length=255, blank=True)
    about_title = models.CharField(max_length=100)
    about_sub_title = RichTextField()



    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name = _('Home')
        verbose_name_plural = _('Homes')


