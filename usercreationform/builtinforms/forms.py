from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    """
    docstring
    """
    password2 = forms.CharField(
        label='Confirm Password(again)', widget=forms.PasswordInput)
    insurance_id = forms.IntegerField(label="Insurance id", placeholder="type")

    class Meta:
        model = User
        fields = {'username', 'email', 'first_name',
                  'last_name', 'insurance_id'}
        lables = {'email': 'Email'}
