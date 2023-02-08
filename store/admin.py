from django.contrib import admin
from store.models import Category,Products,Carts,Reviews,Orders,Offers

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Carts)
admin.site.register(Reviews)
admin.site.register(Orders)
admin.site.register(Offers)