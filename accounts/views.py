from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from . import forms
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.http import HttpResponseRedirect
# Create your views here.

class HomePageTemplateView(TemplateView):

    template_name = "accounts/home.html"

class SignUpView(CreateView):

    template_name = 'registration/signup.html'

    form_class = forms.SignUpForm

    success_url = reverse_lazy("login")
