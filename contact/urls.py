from django.urls import path
from contact import views
from contact.views import ContactFormView

app_name = 'contact'

urlpatterns = [ 
    path('contact/', ContactFormView.as_view(), name='contact'),

]              
               
    

