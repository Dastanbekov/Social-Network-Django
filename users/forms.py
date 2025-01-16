from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        # widgets = {
        #     'bio': forms.Textarea(attrs={'placeholder': 'Расскажите о себе', 'rows': 5}),
        #     'birth_date': forms.DateInput(attrs={'type': 'date'}),
        # }
        # labels = {
        #     'bio': 'Биография',
        #     'birth_date': 'Дата рождения',
        # }