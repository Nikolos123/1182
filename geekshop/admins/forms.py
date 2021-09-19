from django import forms

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User



class UserAdminRegisterForm(UserRegisterForm):

    image = forms.ImageField(widget=forms.FileInput(),required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image','age','first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

class UserAdminProfileForm(UserProfileForm):

    def __init__(self,*args,**kwargs):
        super(UserAdminProfileForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False
        self.fields['age'].widget.attrs['readonly'] = False