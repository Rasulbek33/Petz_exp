from django.urls import path
from blog import views
from blog.views import BlogView

app_name = 'blog'

urlpatterns = [ 
    path('blog/', BlogView.as_view(), name='blog'),

]              
               