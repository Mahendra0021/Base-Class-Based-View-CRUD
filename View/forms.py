from .models import Student
from django import forms
class StudentForm(forms.Form):
    class Meta:
        model = Student
        fields = ['Uname','email','password']
        widgets ={
            'Uname': forms.TextInput(attrs ={'class':'form-control'}),
            'email': forms.EmailInput(attrs ={'class':'form-control'}),
            'password': forms.PasswordInput(attrs ={'class':'form-control'})
        }