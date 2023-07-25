from django.shortcuts import render
from web.models import Category,Item

def index(request):
    items = Item.objects.all()[0:6]
    categories = Category.objects.all()
    context  = {
        'categories' : categories,
        'items' : items,
    }
    return render(request, 'web/index.html',context)
