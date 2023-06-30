from . import views

from django.urls import path 

urlpatterns = [
    path('api/', views.CelebrityCURDView.as_view(), name='api')
]