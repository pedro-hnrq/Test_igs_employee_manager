from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Collaborator


# Bring by the ID of each employee Ex.: curl -H "Accept: application/json" http://127.0.0.1:8000/employee/2/
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

# Noting that to run the command commented above, you have to run it in the terminal: python3 manage.py runserver