from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView)
from .models import Property

# Create your views here.


def index(request):

    return render(request, 'property/home.html')


class PropertyHomeView(TemplateView):

    template_name = 'property/home.html'

    def get_queryset(self):

        queryset = Property.objects.all()

        return queryset

    def get_context_data(self):

        context_data = super().get_context_data()

        context_data['object_list'] = self.get_queryset().order_by(
            '-created_at')[:3]

        return context_data

class PropertyListView(ListView):

    model = Property

class PropertyDetailView(DetailView):

    model = Property
