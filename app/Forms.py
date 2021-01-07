from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import Course, Module, Question

from django.contrib.auth.models import User

class CreateUser_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Course_Form(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name','author','description','materials']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'author': forms.HiddenInput(),
            'description': forms.Textarea(attrs={"class": "form-control"}),
            'materials': forms.URLInput(attrs={'class':"form-control", 'placeholder':"Add a link to more materials (Perhaps a drive link)"}),
        }
    
class User_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
        }

class Module_Form(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['course','name', 'description', 'materials']

        widgets = {
            "course": forms.HiddenInput(),
            "name": forms.TextInput(attrs={'class':"form-control"}),
            "description": forms.Textarea(attrs={'class':"form-control"}),
            'materials': forms.URLInput(attrs={'class':"form-control", 'placeholder':"Add a link to more materials (Perhaps a drive link)"}),
        }

class Question_Form(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

        widgets = {
            'module': forms.HiddenInput(),
            'Q': forms.TextInput(attrs={'class':"form-control"}),
            'opt1': forms.TextInput(attrs={'class':"form-control"}),
            'opt2': forms.TextInput(attrs={'class':"form-control"}),
            'opt3': forms.TextInput(attrs={'class':"form-control"}),
            'opt4': forms.TextInput(attrs={'class':"form-control"}),
            'Reason': forms.TextInput(attrs={'class':"form-control"}),
        }
        
        labels = {
            'Q': "Question",
            'opt1': 'Option 1',
            'opt2': 'Option 2',
            'opt3': 'Option 3',
            'opt4': 'Option 4',
        }