from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import User



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'email',
            'password1',
            'password2',
            'phone',
            'country',
            'zipcode',
            'first_name',
            'last_name',
            'account_category',
            # 'account_tag',
        ]

