from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from users.models import User
from products.models import Product
from .models import CartItem

@api_view(['POST'])
def add_to_cart(request):
    user_id = request.data.get('user_id')
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))

    user = get_object_or_404(User, id=user_id)
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
    
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity

    cart_item.save()

    return Response({"message": "Product added to cart"}, status=status.HTTP_201_CREATED)