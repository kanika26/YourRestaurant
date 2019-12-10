from django.contrib import admin
from .models import dish,UserProfileInfo,Cart,CartObject,onlineorderform

# Register your models here.
admin.site.register(dish)
admin.site.register(UserProfileInfo)
admin.site.register(Cart)
admin.site.register(CartObject)
admin.site.register(onlineorderform)

