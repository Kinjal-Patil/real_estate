from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from myapp.models import Project, Flat


class Home(ListView):
    model = Project
    template_name = "test.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['flats'] = Flat.objects.all()
        return kwargs
