from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class UpdateProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['profile_image', 'bio']

class PasswordChangeForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder" : "Old Password",}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder" : "New Password",}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', "placeholder" : "Confirm Password",}))

    class Meta:
        model = User
        fields = ['new_password1']