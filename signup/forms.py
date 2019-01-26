
from django import forms
from home.models import MyUser


class SignupModelForm(forms.ModelForm):
    class Meta:
        model = MyUser

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'gender',
            'phone_number',
            'password'
        ]