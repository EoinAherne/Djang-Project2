from django.shortcuts import render 

# Create your views here.
def get_djang_list(request):
    return render(request, 'djang/djang_list.html')

     