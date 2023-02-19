from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    typeof = forms.CharField(required=True)
    class Meta:
	    model = User
	    fields = ("username", "email", "password1","typeof")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.typeof = self.cleaned_data['typeof']
        if commit:
            user.save()
        return user