# users/urls.py
from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    # this one shows the profile of the current logged in user,
    # but does not display profile of other users
    # ^(shows other profiles as the current user's profile)
    # path('<username>/', views.ProfileView.as_view(), name='user_profile'),

    # display profile of <username>
    path('<username>/', views.get_user_profile, name='u_profile'),
]
