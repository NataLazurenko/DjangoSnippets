from django.forms import ModelForm
from django import forms
from MainApp.models import Snippet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code']
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']




