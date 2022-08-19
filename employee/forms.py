from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from employee.models import Employee


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        ]

class LogInForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class EmployeeRegistrationForm(ModelForm):
    class Meta:
        model = Employee
        fields="__all__"

        widgets={

            "employee_name": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),


        }


