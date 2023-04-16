from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_0name', 'last_name', 'email', 'phone', 'avatar', 'years_of_experience', 'skills']
