from .models import Book
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["name", "desc", "img"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "id": "name"}),
            "desc": forms.Textarea(attrs={"class": "form-control", "id": "desc"}),
            "img": forms.FileInput(attrs={"class": "form-control", "id": "img"}),
        }

class Register(UserCreationForm):
    is_staff = forms.BooleanField(initial=False,required=False)
    class Meta:
        model = User
        fields =['username','email','password1','password2','is_staff']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),        
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),      
             }