from django.shortcuts import render, redirect
from users.models import CustomUser
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Loads view
def demoView(request):
    # Get the current logged in user
    recipient = request.user

    send_demo_mail(request, recipient)
    return render(request, 'demo_success.html', {"recipient": recipient})

# Sends a demo message to user's email
# Does not render page
def send_demo_mail(request, recipient):

    # Fill details of email
    subject = "[Quirky Messenging Service] Demo Message"
    message = "Hello!\
        You have requested a demo message to be sent to this email.\
        This is how received messages will look like.\
        Please be wary of links (do not click on any links if you are not 100% certain)."
    to_email = [recipient.email]

    try:
        send_mail(subject, message, '', to_email, fail_silently=False)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    
    # if message has been sent out successfully,
    # redirect user to success page ??
