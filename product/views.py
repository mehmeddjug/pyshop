from django.shortcuts import get_object_or_404, redirect, render

from product.forms import ProductForm
from product.models import Product


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_products')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def get_products(request):
    products = Product.objects.all()
    return render(
        request,
        'get_products.html',
        {'products': products}
    )


def get_product_by_id(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(
        request,
        'get_product_by_id.html',
        {'product': product}
    )


def update_product_by_id(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('get_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'create_product.html', {'form': form})


def delete_product_by_id(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('get_products')
    return render(
        request,
        'delete_product.html',
        {'product': product}
    )
