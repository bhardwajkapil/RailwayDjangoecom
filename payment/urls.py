from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name="place_order"),
    path('billing_order/', views.billing_order, name="billing_order"),
    path('process_order/',views.process_order,name="process_order"),

]