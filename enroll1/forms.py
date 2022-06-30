from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta: #it must be added when we use forms class.
      model=User  #add user class into models.
      fields=['name','email','password']  #fields of user class.
      widgets={
          'name':forms.TextInput(attrs={'class':'form-control'}),
          'email': forms.EmailInput(attrs={'class': 'form-control'}),
          'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'})
      }

