# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.exceptions import ValidationError

# Code taken from Ahmed's github:
# https://github.com/AhmedRafikDjerah/Django-registration/blob/master/account/forms.py
class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField( 
        widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'required': True})
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
        help_texts = {
            'email': 'Received messages will be sent to this email. Email be changed later.'
        }

    # Validating password
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password1']:
            raise ValidationError("Passwords do not match.")

        return cd['password2']

class CustomUserChangeForm(UserChangeForm):
    # username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
    #                             label="Username", error_messages={
    #         'invalid': ("This value must contain only letters, numbers and underscores.")})

    # password (the variable) overwrites/loads? the password
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs=dict(required=True, max_length=30)), 
            label="Password") #label is displayed to user

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'required': True})
        }
    # Validate password before user can modify profile (username, email)
    # code not working, gives a keyvalue error
    # def clean(self):
        # if 'password' in self.cleaned_data:
            # p = CustomUser.objects.get(username__iexact=self.initial['username'])
            # if not p.check_password(self.cleaned_data['password']):
            #     raise forms.ValidationError("Password is invalid.")

        #check if password that user entered does not match password stored on account
        #most recent attempt
        # password_entered = self.data.get("password")
        # if password_entered != self.clean_password(): #self.initial["password"]:
        #     raise forms.ValidationError("Password is invalid.")
        # return self.cleaned_data

    # this doesn't work (less well than the above code)
    # def clean(self):
    #     cleaned_data = super(CustomUserChangeForm, self).clean()
    #     password = cleaned_data['password']
    #     if password != self.initial["password"]:
    #         raise forms.ValidationError("Password is invalid.")
    #     return cleaned_data