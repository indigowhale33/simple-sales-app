from rest_framework import serializers
from restapi.models import Customer, Cart, Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Product
        fields = ('id', 'product_name', 'our_price', 'original_price','image_url' )  #cart

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ( 'CustomerID', 'lastInitial', 'firstname')#, 'cart')
    
class CartSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.CustomerID', read_only=True)
    class Meta:
        model = Cart
        fields = ('id', 'username', 'user', 'items') ##'product, id
#        depth = 1



