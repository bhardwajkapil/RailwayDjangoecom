from django.contrib import admin
from .models import ShippingAddress,Order,OrderItem
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(ShippingAddress)
admin.site.register(Order)
#admin.site.register(OrderItem)


class OrderItemInline(admin.StackedInline):
    model=OrderItem
    extra=0


class OrderAdmin(admin.ModelAdmin):
    model=Order
    inlines=[OrderItemInline]
   # fields=["date_ordered"]
    #readonly_field=["date_ordered"]
   

from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

admin.site.unregister(Order)
admin.site.register(Order,OrderAdmin)