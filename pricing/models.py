from django.db import models
from contact.abstract import BaseModel



class Our_plans(BaseModel):
    title = models.CharField(max_length=100, help_text='title')
    sub_title = models.CharField(max_length=255, help_text='sub_title')
    img = models.ImageField(upload_to='Our_plans/%Y/%m/%d', help_text='image')
    


    def __str__(self) -> str:
        return self.title
    

class Pricing(BaseModel):
    direction = models.CharField(max_length=50, help_text='direction')
    price = models.IntegerField()
    species = models.CharField(max_length=50, help_text='species')


    def __str__(self) -> str:
        return self.direction
    
    class Meta:
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricings'