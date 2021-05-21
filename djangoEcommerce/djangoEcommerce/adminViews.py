from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from core.models import categories
from django.views.decorators.csrf import csrf_protect
from django.contrib.messages.views import SuccessMessageMixin


@login_required(login_url="/admin/")
def admin_home(request):
    return render(request, "admin_templates/home.html")


class categoriesListView(ListView):
    model = categories
    template_name = 'admin_templates/category_list.html'


class categoriesCreateView(SuccessMessageMixin, CreateView):
    model = categories
    success_message = "Category Added!"
    fields = '__all__'
    template_name = "admin_templates/category_create.html"


class categoriesUpdateView(SuccessMessageMixin, UpdateView):
    model = categories
    success_message = "Category Updated!"
    fields = '__all__'
    template_name = "admin_templates/category_create.html"
