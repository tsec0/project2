from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import UserProfile
from core.BootstrapFormMixin import BootstarpFormMixin


class SignUpForm(UserCreationForm, BootstarpFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
