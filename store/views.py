from django.shortcuts import render,redirect
from .models import Product,Category
from django.db.models import Q
from store.forms import UserRegisterForm,UpdateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
import json
from cart.cart import Cart
from payment.forms import ShippingAddressForm
from payment.models import ShippingAddress

def home(request):
    products=Product.objects.all().order_by('?')
    for product in products:
        if product.on_sale and  product.sale_price<product.price:
            discount=(product.sale_price*100)/product.price
            discount=int(100-discount)
          #  product["discount"]=discount
            product.discount = discount
    return render(request,'home.html',{"products":products})

def product(request,pk):
    product=Product.objects.get(id=pk)
    similar=Product.objects.filter(category__name=product.category.name).order_by("?")[:6]
   # similar=Category.objects.get(name=product.category.name)
    if product.sale_price<product.price:
        discount=(product.sale_price*100)/product.price
        discount=100-discount
    
    #print(similar)    
    return render(request,"product.html",{"product":product,"discount":discount,"similar":similar})

def search_product(request):
    if request.method=="POST":
       search=request.POST['search']
       products=Product.objects.filter(Q(name__icontains=search) | Q(description__icontains=search) )
       return render(request,"searched_product.html",{"products":products,"search":search})
    else:
       return redirect('search_product') 
    
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST or None)
        if form.is_valid():
           user=form.save()
           login(request,user)
           return redirect('home')
    else:
        form=UserRegisterForm()
    return render(request,'Register.html',{"form":form}) 

def login_user(request):
     error_message=None
     if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            if user.profile.cart_permanent is not None :
                new_cart=json.loads(user.profile.cart_permanent)
                cart=Cart(request)
                for key,value in new_cart.items():
                    cart.add(productid=key,qty=value)
            return redirect('home')
        else:     
          error_message = "Invalid username or password." 
          return redirect('login')
     else:
        return render(request,"Login.html",{"error_message":error_message})
     

def logout_user(request):
    logout(request)
    return redirect('home')   

@login_required
def update_user(request):
    user=User.objects.get(id=request.user.id)
    shipping_info=ShippingAddress.objects.get(user__id=request.user.id)
   # profile=profile.objects.get(user=request.user)
    if request.method=='POST':
        form=UpdateUserForm(request.POST or None,instance=user)
        shipping_form=ShippingAddressForm(request.POST or None,instance=shipping_info)
        if form.is_valid() and shipping_form.is_valid():
           user=form.save()
           shipping_form.save()
           login(request,user)
           return redirect('home')
    else:
        form=UserRegisterForm(instance=user)
        shipping_form=ShippingAddressForm(instance=shipping_info)
    return render(request,"profile.html",{"form":form,"shipping_form":shipping_form})