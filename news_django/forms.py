from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser

class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    email = forms.EmailField(label='Email', max_length=100)
    birthday = forms.DateField(label='Birthday', help_text="dd/mm/yyyy")

    class Meta:
        model = MyUser
        fields = ( 'email', 'first_name', 'last_name', 'birthday')
