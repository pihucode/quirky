# users/urls.py
from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('demo/', views.demoView, name='demo_message'),
    # path('demo/success/', TemplateView.as_view(template_name='demo_success.html'), name='demo_success'),    path('demo/success/', TemplateView.as_view(template_name='demo_success.html'), name='demo_success'),
]
