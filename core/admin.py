from django.contrib import admin
from .models import person, Item, OrderItem
admin.site.register(person)
admin.site.register(Item)
admin.site.register(OrderItem)

