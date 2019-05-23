from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser
from django import forms

# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = CustomUser
#         fields = ('username', 'email')

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password')

class ContactForm(forms.Form):

    # from_email = forms.EmailField(required=True)
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-input', 'required': True}))
    message = forms.CharField( 
        widget=forms.Textarea(attrs={'class': 'form-input', 'required': True}))