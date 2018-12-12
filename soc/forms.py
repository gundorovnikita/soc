from django import forms
from django.contrib.auth.models import User

class UserLogin(forms.Form):
    username = forms.CharField(label='')
    password = forms.CharField(label='', widget=forms.PasswordInput)

class UserRegistration(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Enter Password Here...'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Confirm Password...'}))
    class Meta:
        model = User
        fields = {
            'username',
            'email',
        }
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise form.ValidationError('Password Mismatch')
        return confirm_password
