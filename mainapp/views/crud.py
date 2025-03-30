from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from mainapp.models import *
from django import forms

class PartListView(ListView):
    model = Part
    template_name = 'mainapp/part_list.html'
    context_object_name = 'part_list'

class PartDetailView(DetailView):
    model = Part
    template_name = 'mainapp/part_detail.html'
    context_object_name = 'part'

class PartCreateView(CreateView):
    model = Part
    fields = ['part_number', 'description', 'container']

    template_name = 'mainapp/part_form.html'
    success_url = reverse_lazy('part_list')

class PartUpdateView(UpdateView):
    model = Part
    fields = ['part_number', 'description', 'container']

    template_name = 'mainapp/part_form.html'
    success_url = reverse_lazy('part_list')

class PartDeleteView(DeleteView):
    model = Part
    template_name = 'mainapp/part_confirm_delete.html'
    success_url = reverse_lazy('part_list')

class ContainerListView(ListView):
    model = Container
    template_name = 'mainapp/container_list.html'
    context_object_name = 'container_list'

class ContainerDetailView(DetailView):
    model = Container
    template_name = 'mainapp/container_detail.html'
    context_object_name = 'container'

class ContainerCreateView(CreateView):
    model = Container
    fields = ['name', 'description', 'parent_container']

    template_name = 'mainapp/container_form.html'
    success_url = reverse_lazy('container_list')

class ContainerUpdateView(UpdateView):
    model = Container
    fields = ['name', 'description', 'parent_container']

    template_name = 'mainapp/container_form.html'
    success_url = reverse_lazy('container_list')

class ContainerDeleteView(DeleteView):
    model = Container
    template_name = 'mainapp/container_confirm_delete.html'
    success_url = reverse_lazy('container_list')
