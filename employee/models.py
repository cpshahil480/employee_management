from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    employee_name=models.CharField(max_length=20)
    image=models.ImageField(upload_to="images",null=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=15)
    phone=models.PositiveIntegerField()
    address=models.CharField(max_length=200)
