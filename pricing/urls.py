from django.urls import path
from pricing import views


app_name = 'pricing'

urlpatterns = [ 
    path('pricing/', views.pricing, name='pricing'),

]              
               