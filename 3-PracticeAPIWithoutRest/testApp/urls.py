from django.urls import path 
from . import views

urlpatterns = [
    path('api/', views.CelebrityView.as_view(), name='celebrities'),
    path('api/<int:pk>/', views.CelebrityDetailView.as_view(), name='celebrity'),
]