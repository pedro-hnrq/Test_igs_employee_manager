from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employees, name='employee'),
    path('employee/<int:id>/', views.employee, name='employee_detail'),
    path('employee/list', views.employee_list, name='employee_list'),
    path('employee/add/', views.add_employee, name='add_employee'),
    path('employee/edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('employee/delete/<int:id>/', views.delete_employee, name='delete_employee'),

]