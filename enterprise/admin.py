from django.contrib import admin
from .models import Collaborator, Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display =('id','description')
    
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ('id','department', 'name', 'email', 'address')
    list_filter = ('department',)
    search_fields = ('name', 'email', 'department__name', 'address')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Collaborator, CollaboratorAdmin)

