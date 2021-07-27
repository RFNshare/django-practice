from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import *
from django.urls import reverse_lazy
from django.views import View
# Create your views here.
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import *
from .models import *


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'autos/autos_list.html')


def autos_crud(request):
    return render(request, 'autos/index.html')


class MakeListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = MakeCreate
    template_name = 'autos/make_list.html'
    success_message = 'Make Created Successfully'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['make_count'] = MakeCreate.objects.all().count()
        return context


class MakeCreateView(LoginRequiredMixin, View):
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
            messages.success(request, 'Make Created Successfully')
            return redirect('autos:make_list')
        ctx = {
            'form': form
        }
        return render(request, 'autos/make_create.html', ctx)


class MakeUpdateView(LoginRequiredMixin, View):
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
            return redirect('autos:autos_list')
        ctx = {
            'form': form
        }
        return render(request, 'autos/make_create.html', ctx)


class MakeDeleteView(LoginRequiredMixin, View):
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


class AutosListView(LoginRequiredMixin, ListView):
    model = AutosCreate
    template_name = 'autos/autos_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['make_count'] = MakeCreate.objects.all().count()
        return context


class AutosCreateView(LoginRequiredMixin, View):
    template = 'autos/autos_create.html'
    success_url = reverse_lazy('autos:autos_list')

    def get(self, request):
        form = AutosForm
        ctx = {
            'form': form,
            'create': 'create'
        }
        return render(request, self.template, ctx)

    def post(self, request):
        form = AutosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        ctx = {
            'form': form,
            'create': 'create'
        }
        return render(request, self.template, ctx)


class AutosUpdateView(LoginRequiredMixin, View):
    template = 'autos/autos_create.html'

    def get(self, request, pk):
        autos = get_object_or_404(AutosCreate, pk=pk)
        form = AutosForm(instance=autos)
        ctx = {
            'form': form,
            'autos': autos,
            'update': 'update'
        }
        return render(request, 'autos/autos_create.html', ctx)

    def post(self, request, pk):
        autos = AutosCreate.objects.get(id=pk)
        form = AutosForm(request.POST, instance=autos)
        if form.is_valid():
            form.save()
            return redirect('autos:autos_list')
        ctx = {
            'form': form,
            'update': 'update'
        }
        return render(request, self.template, ctx)


class AutosDeleteView(LoginRequiredMixin, View):
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
