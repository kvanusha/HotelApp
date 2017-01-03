from django.contrib import admin

# Register your models here.
from .models import Room,Menu,Food,Order,Sweets,Beverages,Chats,User
# Register your models here.
admin.site.register(Room)
admin.site.register(Menu)
admin.site.register(Food)
admin.site.register(Sweets)
admin.site.register(Beverages)
admin.site.register(Chats)
admin.site.register(Order)
admin.site.register(User)
