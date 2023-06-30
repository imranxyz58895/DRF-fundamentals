from django.urls import path 
from . import views

urlpatterns = [
    path('HttpApi/', views.employee_data_HttpView, name='http-api'),
    path('jsonApi/', views.employee_data_JSONView, name='employe'),
    path('api/', views.JSONView.as_view(), name='employee-api'),
    path('mixinapi/', views.MixinResponse.as_view(), name='mixin-api'),
]