from django.urls import path
from . import views

app_name = 'adoption'

urlpatterns = [
    path('adoption/', views.adoption, name='adoption'),
    path('adoption_detail/<int:id>/', views.detail_page, name='adoption_detail'),
]