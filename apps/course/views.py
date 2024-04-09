from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializer import ProductSerializers , CategorySerializer
from .models import Product , Category

@api_view()
def products(request):

    product = Product.objects.all()
    serializer = ProductSerializers(product, many = True)

    return Response(serializer.data)

@api_view()
def categories(request):
    cat = Category.objects.all()
    serializer = CategorySerializer(cat , many =True)

    return Response(serializer.data)