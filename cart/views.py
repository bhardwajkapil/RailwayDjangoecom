from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from .cart import Cart
from store.models import Product
from django.core.mail import send_mail



# Create your views here.
def cart_summary(request):
   cart= Cart(request)
   total=cart.cart_total()
   cart_prods=cart.get_prods()
   cart_qty=cart.get_qty()
   #print(cart_prods)
   return render(request,"cart_summary.html",{"products":cart_prods,"cart_qty":cart_qty,"total":total})

def cart_add(request):
   cart= Cart(request)
   productid=str(request.POST.get('productid'))
   product_qty=str(request.POST.get('product_qty'))
   cart.add(productid=productid,qty=product_qty)
   cart_qty=cart.__len__()
   #request.session.modified = True
   return  JsonResponse({
      'qty':cart_qty
   })


def cart_update(request):
   cart= Cart(request)
   if request.POST.get("action")=="post":
      productid=str(request.POST.get('productid'))
      product_qty=int(request.POST.get('product_qty'))
      cart.update_cart(productid=productid,qty=product_qty)
      return redirect('cart_summary')


def cart_delete(request,pk):  
     cart= Cart(request)   
     cart.delete_item(pk) 
     shipping_info=request.session.get('shipping_info')
     shipping_email=shipping_info['shipping_email']
     send_mail(
         subject='Hello fromshopeasy',        
         message=' i just noticed ki aapne jo samman cart me tha usko delte kiya ha , chupchap usko wapas daalo aur abhi kharido minute se pahle nahi anzam soch ke rakhna',     # Plain text message
         from_email='kb1101999@gmail.com',  
         recipient_list=[shipping_email],  
         fail_silently=False,                
      )

     return redirect("cart_summary")

def cart_total(request):
    cart= Cart(request)
    return cart.cart_total()