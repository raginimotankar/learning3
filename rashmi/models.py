from django.db import models

class Rashmi(models.Model):
    
    employeename=models.CharField(max_length=255)
    employeeage=models.CharField(max_length=255)
    employeeid=models.CharField(max_length=255)