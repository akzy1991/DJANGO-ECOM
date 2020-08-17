from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


def index(request):
    context = {'title': 'Products'}
    return render(request, 'products/all_products.html', context)
