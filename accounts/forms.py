from django import forms

class LoginForm(forms.Form):
    """
    Used by the user to enter login credentials
    """
    user_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)