from django.urls import path
from .views import employee, employees


urlpatterns = [
    path('employee/', employees, name='employee_list'),
    path('employee/<int:id>/', employee, name='employee_detail'),
]