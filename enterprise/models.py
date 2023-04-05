from django.db import models

class Department (models.Model):    
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.description
    
class Collaborator (models.Model):

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100, default='')    
    email = models.EmailField(max_length=200)
    
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name