from django.http import *
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages


# Create your views here.

def cat_list(request):
    cats = Cat.objects.all()
    breed_count = Breed.objects.all().count()
    ctx = {
        'cats': cats,
        'breed_count': breed_count
    }
    return render(request, 'cats/cats_list.html', ctx)


def cat_create(request):
    form = CatsForm
    ctx = {
        'form': form,
        'create': 'create'
    }
    if request.method == 'POST':
        form = CatsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cat Created Successfully')
            return redirect('cats:all')
    return render(request, 'cats/cats_create.html', ctx)


def cat_update(request, pk):
    cat = Cat.objects.get(id=pk)
    form = CatsForm(instance=cat)
    ctx = {
        'form': form,
        'update': 'update'
    }
    if request.method == 'POST':
        form = CatsForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cat Updated Successfully')
            return redirect('cats:all')
    return render(request, 'cats/cats_create.html', ctx)


def cat_delete(request, pk):
    cat = Cat.objects.get(id=pk)
    if request.method == 'POST':
        cat.delete()
        messages.success(request, 'Cat Deleted Successfully')
        return redirect('cats:breeds_all')
    ctx = {
        'cat': cat
    }
    return render(request, 'cats/cat_delete.html', ctx)


def breeds_list(request):
    breeds = Breed.objects.all()
    ctx = {
        'breeds': breeds
    }
    return render(request, 'cats/breed_list.html', ctx)


def breeds_create(request):
    form = BreedForm
    ctx = {
        'form': form
    }
    if request.method == 'POST':
        form = BreedForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Breed Created Successfully')
            return redirect('cats:breeds_all')
    return render(request, 'cats/breed_create.html', ctx)


def breed_update(request, pk):
    breed = Breed.objects.get(id=pk)
    form = BreedForm(instance=breed)
    ctx = {
        'form': form
    }
    if request.method == 'POST':
        form = BreedForm(request.POST, instance=breed)
        if form.is_valid():
            form.save()
            messages.success(request, 'Breed Updated Successfully')
            return redirect('cats:breeds_all')
    return render(request, 'cats/breed_create.html', ctx)


def breed_delete(request, pk):
    breed = Breed.objects.get(id=pk)
    if request.method == 'POST':
        breed.delete()
        messages.success(request, 'Breed Deleted Successfully')
        return redirect('cats:breeds_all')
    ctx = {
        'breed': breed
    }
    return render(request, 'cats/breed_delete.html', ctx)
