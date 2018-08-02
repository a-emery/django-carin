from django import forms
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password, get_password_validators
from django.conf import settings


class UserForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(UserForm, self).__init__(*args, **kwargs)
        self.request = request
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True
        self.fields['password'] = forms.CharField(required=True, label='Password', label_suffix='', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'login-form-input'}))
        self.fields['password_confirm'] = forms.CharField(required=True, label='Confirm Password', label_suffix='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'login-form-input'}))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
                'class': 'login-form-input'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
                'class': 'login-form-input'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'E-mail',
                'class': 'login-form-input'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
                'class': 'login-form-input'
            })
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'E-mail'
        }

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        validators = get_password_validators(settings.AUTH_PASSWORD_VALIDATORS)
        validate_password(password, user=None, password_validators=validators)
        if password and password_confirm:
            if password != password_confirm:
                msg = "The two password fields must match."
                self.add_error('password', msg)
        return cleaned_data

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        email = self.cleaned_data["email"]
        user.username = email
        if commit:
            user.save()
            login(self.request, user)
        return user
