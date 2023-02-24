from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input-box',
            'name': 'username',
            'placeholder':'Enter username',
        }),
    )
    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'name': 'password2',
            'id': 'floatingConfirmPassword',
            'placeholder':'Confirm password',
        }),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'input-box',
            'name': 'password1',
            'placeholder':'Enter password',
        }),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'input-box',
            'name': 'email',
            'placeholder':'Enter Mail id',
        }),
    )
    typeof = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input-box',
            'name': 'typeof',
            'placeholder':'type',
        }),
    )
    class Meta:
	    model = User
	    fields = ("username", "email","password1","typeof")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.typeof = self.cleaned_data['typeof']
        if commit:
            user.save()
        return user