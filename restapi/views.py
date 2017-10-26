from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse, JsonResponse
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
 
