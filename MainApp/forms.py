from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code']

class UserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

    def save(self, commit=True):
        user = super(UserProfile, self).save(commit=False)
        if commit:
            user.save()
        return user
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
        #password1 = forms.CharField(label="password", widget=forms.PasswordInput)
        #password2 = forms.CharField(label="password confirm", widget=forms.PasswordInput)
    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user





