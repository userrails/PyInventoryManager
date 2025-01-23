from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Category
from .forms import CategoryForm

def index(request):
    categories = Category.objects.all()
    return render(request, 'categories/index.html', {'categories': categories})

def detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'categories/detail.html', {'category': category})

def create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories:index')
    else:
        form = CategoryForm()
    return render(request, 'categories/form.html', {'form': form})

def update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories:index')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/form.html', {'form': form})

def delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
    return redirect('categories:index')

def products(request):
    products = Product.objects.select_related('category').all()
    return render(request, 'categories/products.html', {
        'products': products
    })
