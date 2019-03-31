# users/views.py
# from django.urls import reverse_lazy
# from django.views import generic
# from users.forms import CustomUserCreationForm
# from django.template.response import TemplateResponse #test
from django.shortcuts import render
from users.models import CustomUser

#test
# def testdex(request):
#     args = {}
#     args['mytext'] = "<b>hello world</b>"
#     return TemplateResponse(request, 'profile.html', args)

# displays profile of the current logged in User
# class ProfileView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     template_name = 'profile.html'

# displays profile of the username passed in URL
def get_user_profile(request, username):
    user = CustomUser.objects.get(username=username)
    return render(request, 'profile.html', {"user":user})
