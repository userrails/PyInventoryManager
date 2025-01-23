from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Category, Product
from .forms import CategoryForm

def index(request):
    stocks = Category.objects.all()
    return render(request, 'stocks/index.html', {'stocks': stocks})

def detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'stocks/detail.html', {'category': category})

def create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stocks:index')
    else:
        form = CategoryForm()
    return render(request, 'stocks/form.html', {'form': form})

def update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('stocks:index')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'stocks/form.html', {'form': form})

def delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
    return redirect('stocks:index')

def products(request):
    products = Product.objects.select_related('category').all()
    return render(request, 'stocks/products.html', {
        'products': products
    })
