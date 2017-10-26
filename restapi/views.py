from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from restapi.serializers import CartSerializer, CustomerSerializer, ProductSerializer

from restapi.models import Cart, Customer, Product
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'customer': reverse('customer-list', request=request, format=format),
        'product': reverse('product-list', request=request, format=format),
        'cart': reverse('cart-list', request=request, format=format)
    })

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'CustomerID'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
#    lookup_field = 'product_name'


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def list(self, request):
        queryset = Cart.objects.all()
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)
 
 #   def destroy(self, validated_data, *args, **kwargs):
 #       try:
 #           instance = self.get_object()
 #           print(instance)
 #           print(validated_data)
   
 #   def create(self, validated_data):
 #       print([i.user.CustomerID for i in Cart.objects.all()])
 #       print(Cart.objects.get(user= str(validated_data.data['user']), items= str(validated_data.data['items'])))
 
        #cart, created = Cart.objects.get_or_create( user = validated_data.data['user'], defaults={'items' : validated_data.data['items'] Cart.objects.get(user= validated_data.data['user'], items= validated_data.data['items']).items})
  #      return cart
  #      print(Cart.objects.get(user= '1', items='4'))
  #      print(validated_data.data)
  #      print(validated_data.get('user'))
  #      print(validated_data.get('items'))
