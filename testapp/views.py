from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from testapp.models import Company

from django.urls import reverse_lazy
# Create your views here.

class CompanyCRUDListView(ListView):
    model = Company

    # template_name: str = "company_list.html"
    # context_object_name: str = "company_list"

class ComaontCRUDDetailView(DetailView):
    model = Company

    # template_name = "company_detail.html"
    # context_object_name = "company" / "object"

class CompanyCRUDCreateView(CreateView):
    model = Company
    fields = "__all__"

    # template_name: str = "company_form.html"

class CompanyCRUDUpdateView(UpdateView):
    model = Company
    fields = "__all__" 

class CompanyCRUDDeleteView(DeleteView):
    model = Company

    success_url = reverse_lazy("List")
