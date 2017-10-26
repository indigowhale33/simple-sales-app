from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from rest_framework import routers
from restapi import views
from restapi.views import CustomerViewSet, ProductViewSet, CartViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

#@api_view(['GET'])
#def api_root(request, format=None):
#    return Response({
#        'customer-list': reverse('customer-list', request=request, format=format)
#        'customer-detail': reverse('customer-detail', request=request, format=format)
 #       'product': reverse('product-list', request=request, format=format)
#        'product-detail': reverse('product-detail', request=request, format=format)
  #  })

customer_list = CustomerViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

customer_detail = CustomerViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


product_list = ProductViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

product_detail = ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


cart_list = CartViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

cart_detail = CartViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
#urlpatterns = [
#    url(r'^customer/', views.customer_detail.as_view(), name='customer-detail'),
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#]

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^customer/$', customer_list, name='customer-list'),
    url(r'^customer/(?P<CustomerID>[a-z0-9A-Z]+)/$', customer_detail, name='customer-detail'),
    url(r'^product/$', product_list, name='product-list'),
    url(r'^product/(?P<pk>[0-9]+)/$', product_detail, name='product-detail'),
    url(r'^cart/$', cart_list, name='cart-list'),
    url(r'^cart/(?P<pk>[a-z0-9A-Z]+)/$', cart_detail, name='cart-detail'),

])
