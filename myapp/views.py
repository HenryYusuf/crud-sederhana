# from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Dokumen
from .forms import DokumenForm

# READ (List)
class DokumenListView(ListView):
    model = Dokumen
    template_name = 'dokumen_list.html'
    context_object_name = 'dokumen_list'

# CREATE
class DokumenCreateView(CreateView):
    model = Dokumen
    form_class = DokumenForm
    template_name = 'dokumen_form.html'
    success_url = reverse_lazy('dokumen-list')

# UPDATE
class DokumenUpdateView(UpdateView):
    model = Dokumen
    form_class = DokumenForm
    template_name = 'dokumen_form.html'
    success_url = reverse_lazy('dokumen-list')

# DELETE
class DokumenDeleteView(DeleteView):
    model = Dokumen
    template_name = 'dokumen_confirm_delete.html'
    success_url = reverse_lazy('dokumen-list')
