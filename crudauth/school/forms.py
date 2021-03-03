from django import forms
from .models import Student
from django.contrib.auth import authenticate


class StudentRegisterationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        fields = ['username', 'email', 'password', 'age']


class StudentLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

    # class Meta:
    #     model = Student

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')
    #     user = authenticate(username, password)
    #     if not user:
    #         raise forms.ValidationError(
    #             "Sorry, that login was invalid. Please try again.")
    #     return self.cleaned_data
