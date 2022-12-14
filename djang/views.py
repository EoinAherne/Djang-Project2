from django.shortcuts import render, redirect, get_object_or_404
from.models import Item
from .forms import ItemForm

# Create your views here.


def get_djang_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'djang/djang_list.html', context)


def add_item(request):
    if request.method == 'POST':
        form  = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_djang_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'djang/add_item.html', context)

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form=ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_djang_list')

    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'djang/edit_item.html', context)

def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_djang_list')
  