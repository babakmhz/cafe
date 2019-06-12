from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from mainApp.models import category, customCategory, product
from mainApp.serializers import getCustomCategoriesSerializer, getProductsSerializer


class getCategories(generics.ListAPIView):
    serializer_class = getCustomCategoriesSerializer
    queryset = category.objects.all()


class getProducts(generics.ListAPIView):
    serializer_class = getProductsSerializer
    queryset = product.objects.all()
    # def get_serializer_class(self):

    #     return getCustomCategoriesSerializer
