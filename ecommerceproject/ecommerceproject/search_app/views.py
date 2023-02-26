import requests

from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

# Create your views here.


def SearchResult(request):
    products=None
    qurey=None
    if 'q' in request.GET:
        qurey=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=qurey) | Q(description__contains=qurey))

    return render(request,'search.html',{'qurey':qurey,'products':products})





