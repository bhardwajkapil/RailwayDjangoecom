from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from store.models import Product
import datetime


# Create your models here.

class ShippingAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    shipping_full_name=models.CharField(max_length=50)
    shipping_phone=models.CharField(max_length=20,null=True,blank=True)
    shipping_email=models.EmailField(max_length=50,null=True,blank=True)
    shipping_address1=models.CharField(max_length=100)
    shipping_address2=models.CharField(max_length=100,null=True,blank=True)
    shipping_city=models.CharField(max_length=20)
    shipping_state=models.CharField(max_length=20,null=True,blank=True)
    shipping_zipcode=models.CharField(max_length=20)
    shipping_country=models.CharField(max_length=20,null=True,blank=True)

def create_shipping(sender,instance,created, **kwrgs):
    if created:
        shipping=ShippingAddress(user=instance)
        shipping.save()


post_save.connect(create_shipping,sender=User)    

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=13,default=9999999999)
    ShippingAddress=models.CharField(max_length=500)
    amount_paid=models.DecimalField(decimal_places=2,max_digits=7)
    date_ordered=models.DateTimeField(auto_now_add=True)
    date_shipped=models.DateTimeField(blank=True,null=True)#jab shipped hoga tab auto. generate krenge signals ki mdad se
    shipped=models.BooleanField(default=False)

    def __str__(self):
        return f'#order-{self.id}'
    
@receiver(pre_save , sender=Order)
def handler(sender,instance,**kwrgs):
    if instance.pk:
        prev=sender._default_manager.get(id=instance.id)
        if not prev.shipped and instance.shipped:
            instance.date_shipped=datetime.datetime.now()
            

class OrderItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.IntegerField(default=1)
    price=models.DecimalField(decimal_places=2,max_digits=7)

    def __str__(self):
        return f'#orderItem-{self.id}'


