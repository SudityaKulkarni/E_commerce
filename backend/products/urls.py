from django.contrib import admin
from django.urls import path
from .views import search_products

urlpatterns = [
    path('search/<str:search_term>/', search_products, name='search-products'),  # URL for searching products

]