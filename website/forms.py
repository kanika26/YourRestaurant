
from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields=('__all__')


class onlinefoodorderform(forms.Form):
    name = forms.CharField(max_length=400)
    address = forms.CharField(max_length=400)
    city = forms.CharField(max_length=100)
    zipcode = forms.CharField(max_length=8)
    state = forms.CharField(max_length=200)
    phoneno = forms.CharField(max_length=10)
    email = forms.EmailField()


