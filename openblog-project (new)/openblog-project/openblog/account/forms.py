from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']
        widget={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "user_name":forms.TextInput(attrs={"class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"class":"form-control"}),
            "password2":forms.PasswordInput(attrs={"class":"form-control"}),

        }
class LogForm(forms.Form):
    uname=forms.CharField(max_length=100,label="Enter username",widget=forms.TextInput(attrs={"class":"form-control"}))        
    psw=forms.CharField(max_length=100,label="Enter password",widget=forms.PasswordInput(attrs={"class":"form-control"}))        
