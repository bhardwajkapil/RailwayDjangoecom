from django.urls import path,include
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name="place_order"),
    path('billing_order/', views.billing_order, name="billing_order"),
    path('process_order/',views.process_order,name="process_order"),
    path('paypal',include("paypal.standard.ipn.urls")),
    path('payment_success',views.payment_success,name="payment_success"),
    path('payment_fail',views.payment_fail,name="payment_fail"),

]