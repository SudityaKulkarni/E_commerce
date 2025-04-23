from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# Create your views here.


@api_view(['GET'])
def search_products(request,search_term):
    
    products = Product.objects.filter(name__icontains = search_term)

    if not products.exists():
        return Response({"message": "No products found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)