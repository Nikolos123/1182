from django import forms

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User



class UserAdminRegisterForm(UserRegisterForm):

    image = forms.ImageField(widget=forms.FileInput(),required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image','first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': False}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': False}))