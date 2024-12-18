from django.shortcuts import render,redirect
from cart.cart import Cart
from .models import ShippingAddress,Order,OrderItem
from .forms import ShippingAddressForm,PaymentForm
#paypal related
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.core.mail import send_mail
import uuid






def place_order(request):
  cart=Cart(request)
  products=cart.get_prods()
  carty=cart.get_qty()
  total=cart.cart_total()
  
  if request.user.is_authenticated:
    shipping_info=ShippingAddress.objects.get(user=request.user.id)
    shipping_form=ShippingAddressForm(request.POST or None, instance=shipping_info)
    return render(request,"order.html",{"products":products,"carty":carty,"total":total,"shipping_form":shipping_form})
  else:
    shipping_form=ShippingAddressForm(request.POST or None)
    return render(request,"order.html",{"products":products,"carty":carty,"total":total,"shipping_form":shipping_form})
  


def billing_order(request):
   if request.method=="POST":
     cart=Cart(request)
     total=cart.cart_total()
     shipping_info=request.POST
     request.session['shipping_info']=shipping_info
     invoice_num=str(uuid.uuid4())
     #getting the host
     host=request.get_host()
     paypal_dict={
       'business':settings.PAYPAL_RECEIVER_EMAIL,
       'amount':total,
       'item_name':"orders",
       'no_shipping':2,
       'invoice':invoice_num,
       'currency_code':'USD',
       'notify_url':'https://{}{}'.format(host,reverse("paypal-ipn")),
       'return_url':'https://{}{}'.format(host,reverse("payment_success")),
       'cancel_return':'https://{}{}'.format(host,reverse("payment_fail"))

     }
     shipping_info=request.session.get('shipping_info')
     shipping_email=shipping_info['shipping_email']
     send_mail(
         subject='Hello fromshopeasy',        
         message='hey kya apke pass paypal ha, kyuki ham ussu se paise lete han bro',     # Plain text message
         from_email='kb1101999@gmail.com',  
         recipient_list=[shipping_email],
         fail_silently=False             
      )
     paypal_form=PayPalPaymentsForm(initial=paypal_dict)
     payment_form=PaymentForm(request.POST or None)
     return render(request,"billing.html",{"total":total,"payment_form":payment_form,"paypal_form":paypal_form})
   else:
     return redirect('home')
   

def process_order(request):
  print("yha tak aaya ha",request.POST)
  if request.method=='POST':
    cart=Cart(request)
    products=cart.get_prods()
    carty=cart.get_qty()
    total=cart.cart_total()
    payment_info=request.POST
    shipping_info=request.session.get('shipping_info')
    shipping_email=shipping_info['shipping_email']
    shipping_full_name=shipping_info['shipping_full_name']
    shipping_phone=shipping_info['shipping_phone']
    shipping_address = f"{shipping_info['shipping_address1']}\n{shipping_info['shipping_city']}\n{shipping_info['shipping_state']}\n{shipping_info['shipping_zipcode']}\n"
    if request.user.is_authenticated:
      create_order=Order(user=request.user,full_name=shipping_full_name,phone=shipping_phone, email=shipping_email,ShippingAddress=shipping_address,amount_paid=total)
      create_order.save()
    
      for product in products:
        for key,value in carty.items():
          if product.on_sale:
            price=product.price
          else:
            price=product.sale_price  
          if int(key)==product.id:
            create_order_item=OrderItem(user=request.user,product=product,quantity=value,price=price,order=create_order)
            create_order_item.save()

            #clearing the cart
            for key in list(request.session.keys()):
               if key=="session_key":
                 del request.session["session_key"]
                 request.user.profile.cart_permanent = ""
                 request.user.profile.save()

    else:  
      create_order=Order(full_name=shipping_full_name,email=shipping_email,phone=shipping_phone,ShippingAddress=shipping_address,amount_paid=total)
      create_order.save()
      for product in products:
        for key,value in carty.items():
          if product.on_sale:
            price=product.price
          else:
            price=product.sale_price  
          if int(key)==product.id:
            create_order_item=OrderItem(product=product,quantity=value,price=price,order=create_order)
            create_order_item.save()
             #clearing the cart
            for key in list(request.session.keys()):
               if key=="session_key":
                 del request.session["session_key"]
                 request.user.profile.cart_permanent = ""
                 request.user.profile.save()

    return render(request,"your_orders.html",{"order": create_order})              
  else:
    return redirect("home")    
     
def payment_success(request):
  return render(request,"payment_success.html",{})

def payment_fail(request):
  return render(request,"payment_fail.html",{})