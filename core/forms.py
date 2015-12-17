from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    password2 = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)

