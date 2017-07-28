from django import forms
from users.models import Users

#just a simple form
class LoginForm(forms.Form):
	userid = forms.IntegerField(min_value=1)
	password = forms.CharField(widget=forms.PasswordInput())