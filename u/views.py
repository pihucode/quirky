# users/views.py
# from django.urls import reverse_lazy
# from django.views import generic
# from users.forms import CustomUserCreationForm
from django.shortcuts import render
from users.models import CustomUser

# displays profile of the current logged in User
# class ProfileView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     template_name = 'profile.html'

# displays profile of the username passed in URL
# cannot use keyword 'user', so 'recipient' is used instead
def get_user_profile(request, username):
    recipient = CustomUser.objects.get(username=username)
    # render passes the recipient object to 'profile.html' template
    # so 'profile.html' can access the 'recipient' object
    return render(request, 'profile.html', {"recipient":recipient})
