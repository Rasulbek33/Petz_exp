from django.urls import path
from our_team import views


app_name = 'our_team'

urlpatterns = [ 
    path('our_team/', views.our_team, name='our_team'),

]              
               