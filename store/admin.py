from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Address)
admin.site.register(Account)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(S_cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Payment)