from django.contrib import admin
from .models import User
# Register your models here.


class AdminUser(admin.ModelAdmin):
  list_display=['id','name','email','password']


admin.site.register(User,AdminUser)
