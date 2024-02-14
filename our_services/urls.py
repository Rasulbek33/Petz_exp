from django.urls import path
from our_services import views
from our_services.views import Our_serviceView

app_name = 'our_services'

urlpatterns = [ 
    path('our_services/', Our_serviceView.as_view(), name='our_services'),

]              
               