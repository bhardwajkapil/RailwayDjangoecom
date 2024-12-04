from store.models import Product,Profile
class Cart():
   def __init__(self,request):
       self.session=request.session
       self.request=request

       cart=self.session.get("session_key")

       if "session_key" not in  request.session:
           cart=self.session["session_key"]={}

       self.cart=cart   

   def add(self, productid, qty):
      # self.request.session.flush()
       if productid in self.cart:
           print("already ha be",self.cart)
           pass
       else:
           self.cart[productid]=int(qty)
           print("pahle nahi thi ab ha",self.cart)
           self.session.modified=True

           if self.request.user.is_authenticated:
               str_cart=str(self.cart)
               str_cart=str_cart.replace('\'',"\"")
               profile=Profile.objects.get(user=self.request.user.id)
               profile.cart_permanent=str_cart
               profile.save()
              

   def __len__(self):
       return len(self.cart)       
   


   def get_prods(self):
       product_ids=self.cart.keys()
       products=Product.objects.filter(id__in=product_ids)
       return products   
   
   def delete_item(self,pk):
       product_id=str(pk)
       if product_id not in self.cart:
           pass
       else:
           del self.cart[product_id]
           self.session.modified=True
        #udate in database too   
       if self.request.user.is_authenticated:
               str_cart=str(self.cart)
               str_cart=str_cart.replace('\'',"\"")
               profile=Profile.objects.get(user=self.request.user.id)
               profile.cart_permanent=str_cart
               profile.save()

   def get_qty(self):
       return self.cart

   def update_cart(self,productid,qty):
       self.cart[productid]=qty       
       self.session.modified=True
       print("updation ke baad",self.cart)
       #also update it in database
       if self.request.user.is_authenticated:
               str_cart=str(self.cart)
               str_cart=str_cart.replace('\'',"\"")
               profile=Profile.objects.get(user=self.request.user.id)
               profile.cart_permanent=str_cart
               profile.save()

   def cart_total(self):
       total=0
       for key,value in self.cart.items():
           product=Product.objects.get(id=key)
           if product.on_sale:
               total+=(product.sale_price*value)
           else:
               total+=(product.price*value)
       return total      
          