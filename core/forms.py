from django import forms
from django.contrib.auth.models import User
from .models import person


class Userprofile(forms.ModelForm):
     class Meta:
            model = person
            fields =('name','gender','address','city','phone')

class Userform(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password')

