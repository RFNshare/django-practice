from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views.generic import ListView


def index(request):
    return render(request, 'autos/index.html')


def autos_crud(request):
    return render(request, 'autos/autos_list.html')


class MakeListView(ListView):
    model = MakeCreate
    template_name = 'autos/make_list.html'


class MakeCreateView(View):
    def get(self, request):
        form = MakeForm
        ctx = {
            'form': form
        }
        return render(request, 'autos/make_create.html', ctx)

    def post(self, request):
        form = MakeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autos:make_list')


class MakeUpdateView(View):
    def get(self, request, pk):
        make_update = MakeCreate.objects.get(id=pk)
        form = MakeForm(instance=make_update)
        ctx = {
            'form': form,
            'make_update': make_update
        }
        return render(request, 'autos/make_create.html', ctx)

    def post(self, request, pk):
        make_update = MakeCreate.objects.get(id=pk)
        form = MakeForm(request.POST, instance=make_update)
        if form.is_valid():
            form.save()
            return redirect('autos:make_list')


class MakeDeleteView(View):
    def get(self, request, pk):
        make = MakeCreate.objects.get(id=pk)
        ctx = {
            'make': make
        }
        return render(request, 'autos/make_delete.html', ctx)

    def post(self, request, pk):
        make = MakeCreate.objects.get(id=pk)
        make.delete()
        return redirect('autos:make_list')


class AutosListView(ListView):
    model = AutosCreate
    template_name = 'autos/autos_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['make_create_count'] = MakeCreate.objects.all().count()
        return context


class AutosCreateView(View):
    def get(self, request):
        form = AutosForm
        ctx = {
            'form': form
        }
        return render(request, 'autos/autos_create.html', ctx)

    def post(self, request):
        form = AutosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autos:autos_list')


class AutosUpdateView(View):
    def get(self, request, pk):
        autos = AutosCreate.objects.get(id=pk)
        form = AutosForm(instance=autos)
        ctx = {
            'form': form,
            'autos': autos
        }
        return render(request, 'autos/autos_create.html', ctx)

    def post(self, request, pk):
        autos = AutosCreate.objects.get(id=pk)
        form = AutosForm(request.POST, instance=autos)
        if form.is_valid():
            form.save()
            return redirect('autos:autos_list')


class AutosDeleteView(View):
    def get(self, request, pk):
        autos = AutosCreate.objects.get(id=pk)
        ctx = {
            'autos': autos
        }
        return render(request, 'autos/autos_delete.html', ctx)

    def post(self, request, pk):
        autos = AutosCreate.objects.get(id=pk)
        autos.delete()
        return redirect('autos:autos_list')
