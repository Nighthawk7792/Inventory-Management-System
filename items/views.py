from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Item
from .forms import ItemForm

def home(request):
    return render(request, 'home.html')

def item_list(request):
    # whatever logic you have
    return render(request, 'items/item_list.html')


def item_detail(request, pk):
    """Show details for a specific item"""
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'items/item_detail.html', {'item': item})

def item_create(request):
    """Create a new inventory item"""
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items:item_list')
    else:
        form = ItemForm()
    return render(request, 'items/item_form.html', {
        'form': form,
        'title': 'Add New Item'
    })

def item_update(request, pk):
    """Update an existing inventory item"""
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items:item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'items/item_form.html', {
        'form': form,
        'title': 'Update Item'
    })

def item_delete(request, pk):
    """Delete an inventory item"""
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('items:item_list')
    return render(request, 'items/confirm_delete.html', {'item': item})
