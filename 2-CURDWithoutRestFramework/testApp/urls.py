from django.urls import path 
from . import views

urlpatterns = [
    path('api/<int:pk>/', views.EmployeDetailView.as_view(), name='employee-api'),
    path('api/', views.EmployeesView.as_view(), name='employees'),
    # path('api/', views.EmployeeFieldsView.as_view())
]