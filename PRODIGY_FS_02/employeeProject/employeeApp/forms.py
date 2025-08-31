from django import forms
from .models import Employee
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput,label ="Confirm Password")

    class Meta:
        model = User
        fields = ["username",'password',"password_confirm"]
    def clean(self):
        cleaned_date= super().clean()   
        password =cleaned_date.get('password') 
        password_confirm = cleaned_date.get('password_confirm')
        #check if password match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Password do not match")
        return cleaned_date


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'position': 'Position',
            'salary': 'Salary',
            'hire_date': 'Hire Date',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'e.g. John',
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'e.g. Doe',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'e.g. john.doe@example.com',
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'e.g. 5551234567',
                'class': 'form-control'
            }),
            'position': forms.TextInput(attrs={
                'placeholder': 'e.g. Software Engineer',
                'class': 'form-control'
            }),
            'salary': forms.NumberInput(attrs={
                'placeholder': 'e.g. 5000.00',
                'class': 'form-control'
            }),
            'hire_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }
