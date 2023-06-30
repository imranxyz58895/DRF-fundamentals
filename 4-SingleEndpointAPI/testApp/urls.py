from . import views 
from django.urls import path 

urlpatterns = [
    path('api/', views.CelebrityView.as_view(), name='celebrity'),
]