from django.db import models
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name= models.CharField(max_length=20)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="uploads/product")
    price=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    description=models.TextField(null=True,blank=True)
    on_sale=models.BooleanField()
    sale_price= models.DecimalField(default=0,decimal_places=2,max_digits=6) 

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name= models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
   
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    adddress=models.TextField()
    phone=models.CharField(max_length=13)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=20,null=True,blank=True)
    address1=models.CharField(max_length=100,null=True,blank=True)
    address2=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=20,null=True,blank=True)
    state=models.CharField(max_length=20,null=True,blank=True)
    zipcode=models.CharField(max_length=20,null=True,blank=True)
    country=models.CharField(max_length=20,null=True,blank=True)
    profile_pic=models.ImageField(upload_to='uploads/profile_pics/',null=True,blank=True)
    cart_permanent=models.CharField(max_length=500,null=True,blank=True)
    createdAt=models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return f'{self.user.username}'

def create_profile(sender,instance,created, **kwrgs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()


post_save.connect(create_profile,sender=User)    


class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='uploads/review',null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=200, blank=False)
    body=models.CharField(max_length=100,blank=False)
    rating=models.IntegerField()
    createdAt=models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f'Comment by {self.user.username} on {self.product.name}'
    