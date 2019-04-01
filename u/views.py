# from django.urls import reverse_lazy
# from django.views import generic
# from users.forms import CustomUserCreationForm

#for get_user_profile()
from django.shortcuts import render
from users.models import CustomUser

# for mail_to() and thanks()
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

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
    form = mail_to(request, recipient)
    return render(request, 'profile.html', {"recipient":recipient, "form":form})

def mail_to(request, recipient):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "[Quirky Messenging Service] " + form.cleaned_data['subject']
            # from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message'] # body message
            to_email = [recipient.email] # email of the user's profile
            try:
                send_mail(subject, message, '', to_email, fail_silently = False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
                # if message has been sent out successfully,
                # redirect user to success page
            return redirect('success')
    return form

def success(request):
    # return HttpResponse('Thank you for your message.')
    return HttpResponse('Your message has been sent!')
