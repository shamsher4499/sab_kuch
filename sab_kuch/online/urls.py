from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('checkout/', views.checkout, name='checkout'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('cart/', views.cart, name='cart'),
    path('products/', views.products, name='products'),
    path('customer/', views.customer, name='customer'),
]