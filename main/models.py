from django.db import models

class Home(BaseModel):
    title = models.CharField(max_length=255, blank=True)