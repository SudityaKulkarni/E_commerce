from django.contrib import admin
from django.urls import path
from .views import add_to_cart

urlpatterns = [
    path('add/',add_to_cart, name='add-to-cart'),  # URL for adding items to the cart
]