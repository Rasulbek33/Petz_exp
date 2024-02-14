from django.urls import path
from blog import views
from adoption.views import AdoptionView

app_name = 'adoption'

urlpatterns = [ 
    path('adoption/', AdoptionView.as_view(), name='adoption'),
    path('adoption_name/', AdoptionView.as_view(), name='adoption_name'),
]              
               