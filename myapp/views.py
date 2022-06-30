from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from myapp.models import Project


class Home(ListView):
    model = Project
    template_name = "test.html"
