from django.contrib import admin
from django.contrib.auth.models import User

from .models import Category,Customer,Product,Order,Profile

# Register your models here.

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)


class ProfileInline(admin.StackedInline):
    model=Profile


class UserAdmin(admin.ModelAdmin):
    model=User
    inlines=[ProfileInline]
    fields=['username','email','first_name','last_name','password']
    extras=0

from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

admin.site.unregister(User)
admin.site.register(User,UserAdmin)