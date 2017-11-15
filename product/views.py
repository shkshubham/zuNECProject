from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from product.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

def product_list(request, template_name='product/index.html'):
    product = Product.objects.all()
    data = {}
    data['object_list'] = product
    return render(request, template_name, data)

def product_create(request, template_name='product/create.html'):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, template_name, {'form':form})

def product_update(request, pk, template_name='product/create.html'):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, template_name, {'form':form})

def product_delete(request, pk, template_name='product/delete.html'):
    product = get_object_or_404(Product, pk=pk)
    if request.method=='POST':
        product.delete()
        return redirect('product_list')
    return render(request, template_name, {'object':product})
