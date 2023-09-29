from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Cart)
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        models=Cart
        fields=['user','id','title','discountprice']