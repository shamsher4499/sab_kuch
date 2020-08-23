from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'online/index.html')

def cart(request):
    return render(request, 'online/cart.html')

def login(request):
    return render(request, 'online/login.html')

def logout(request):
    return render(request, 'online/logout.html')

def register(request):
    return render(request, 'online/register.html')

def checkout(request):
    return render(request, 'online/checkout.html')

def products(request):
    return render(request, 'online/products.html')

def customer(request):
    return render(request, 'online/customer.html')