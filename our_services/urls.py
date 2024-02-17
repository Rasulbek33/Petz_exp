from django.urls import path
from our_services import views


app_name = 'our_services'

urlpatterns = [ 
    path('our_services/', views.our_service, name='our_services'),

]              
               