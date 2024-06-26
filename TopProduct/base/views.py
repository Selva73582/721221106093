from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


from . import models

from . import serializers

@api_view(["GET"])
def getDetails(request):
    companies=request.query_params.getlist("companies")
    categories=request.query_params.getlist("categories")
    top=request.query_params.get("top",None)
    minPrice=request.query_params.get("minPrice",None)
    maxPrice=request.query_params.get("maxPrice",None)


    product=models.Product.objects.all()

    if companies:
        product = product.filter(company__company_name__in=companies)
    if categories:
        product = product.filter(catrgory__category_name__in=categories)
    if minPrice is not None:
        product = product.filter(price__gte=minPrice)
    if maxPrice is not None:
        product = product.filter(price__lte=maxPrice)
    if top is not None:
        product = product.order_by("-rating")[:int(top)]

    print(product)
    
    
    serializer = serializers.ProductSerializer(product, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


