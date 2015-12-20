from django import forms
from django.utils.translation import ugettext as _


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)
    password2 = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password")
        if password != password2:
            self.add_error('password2', _("Passwords are different!"))
            self.add_error('password', _("Passwords are different!"))
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)

