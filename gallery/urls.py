from django.urls import path
from gallery import views
from gallery.views import GalleryView

app_name = 'gallery'

urlpatterns = [ 
    path('gallery/', GalleryView.as_view(), name='gallery'),

]              
               