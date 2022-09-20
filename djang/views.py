from django.shortcuts import render 
from.models import Item
# Create your views here.
def get_djang_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }

    return render(request, 'djang/djang_list.html', context)

     