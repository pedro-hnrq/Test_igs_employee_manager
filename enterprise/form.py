from django import forms
from .models import Collaborator, Department

class CollaboratorForm(forms.ModelForm):
    class Meta:
        model = Collaborator
        fields = ['name', 'email', 'address', 'department']
        
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['description']