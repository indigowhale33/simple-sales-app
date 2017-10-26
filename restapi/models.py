from django.db import models


class Customer(models.Model):
    CustomerID = models.CharField(max_length=12, unique=True)
    lastInitial = models.CharField(max_length=1, null=True)
    firstname = models.CharField(max_length=20)
    
    def __str__(self):
        return '%s (%s %s)' % (self.CustomerID, self.firstname, self.lastInitial)    
#class Cart(models.Model):
#    status = models.CharField(max_length=255, default='')
#    user = models.ForeignKey(Customer, related_name="cart", on_delete=models.CASCADE)



class Product(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=255)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    our_price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.TextField()
####
#    cart = models.ForeignKey(Cart, related_name='products', null=True,on_delete=models.CASCADE)
###
    def __unicode__(self):
        return '%s' % (self.product_name)

    def __str__(self):
        return '%s (%0.2f)' % (self.product_name, self.our_price)

class Cart(models.Model):
    status = models.CharField(max_length=255)
    user = models.ForeignKey(Customer, related_name="cart", on_delete=models.CASCADE, blank=False)
    #items = models.OneToOneField(Product)
    items = models.ForeignKey(Product, default=None, unique=True)
    


