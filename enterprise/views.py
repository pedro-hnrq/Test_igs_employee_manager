from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.messages import constants
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Collaborator, Department
from .form import CollaboratorForm,  DepartmentForm


@api_view(['GET'])
def employee(request, id):
    try:
        collaborator = Collaborator.objects.get(id=id)
        information = {
            'name': collaborator.name,
            'email': collaborator.email,
            'address': collaborator.address,
            'department': collaborator.department.description,
        }
        return Response(information)
    except Collaborator.DoesNotExist:
        return Response({'error': 'Collaborator not found'})


# Getting all employees Ex.: curl -H "Accept: application/json" http://127.0.0.1:8000/employee/
@api_view(['GET'])    
def employees(request):
    collaborators = Collaborator.objects.all()
    information = []
    for collaborator in collaborators:
        information.append({
            'name': collaborator.name,
            'email': collaborator.email,
            'address': collaborator.address,
            'department': collaborator.department.description,
        })
    return Response(information)

# Render the employee list
@api_view(['GET'])
def employee_list(request):
    collaborators = Collaborator.objects.all()
    return render(request, 'employee_list.html', {'collaborators': collaborators})

# Add new employee
@api_view(['GET', 'POST'])
def add_employee(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        return render(request, 'add_employee.html', {'departments': departments})
    elif request.method == 'POST':
        collaborator = Collaborator(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            department_id=request.POST.get('department')
        )
        collaborator.save()
        messages.success(request, 'Employee successfully added..')
        return redirect('employee_list')
    else:
        return render(request, 'add_employee.html')

# Edit existing employee
@api_view(['GET', 'POST'])
def edit_employee(request, id):
    collaborator = get_object_or_404(Collaborator, id=id)
    if request.method == 'GET':
        form = CollaboratorForm(instance=collaborator)
        departments = Department.objects.all()
        return render(request, 'edit_employee.html', {'form': form, 'departments': departments, 'collaborator': collaborator})
    elif request.method == 'POST':
        form = CollaboratorForm(request.POST, instance=collaborator)
        if form.is_valid():
            form.save()
            messages.success(request, constants.WARNING, 'Employee updated successfully.')
            return redirect('employee_list')
    else:
        form = CollaboratorForm(instance=collaborator)
        return render(request, 'edit_employee.html', {'form': form, 'collaborator': collaborator})

# Delete existing employee
@api_view(['GET'])
def delete_employee(request, id):
    collaborator = get_object_or_404(Collaborator, id=id)
    collaborator.delete()
    messages.success(request,constants.INFO, 'Employee removed successfully.')
    return redirect('employee_list')


