from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user.models import User


class UserCreateForm(UserCreationForm):
    """
    Form for creating a new user account.
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)


class UserUpdateForm(forms.ModelForm):
    """
    Form for updating user profile information.
    """

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
