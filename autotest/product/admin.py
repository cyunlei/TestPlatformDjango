from django.contrib import admin
from product.models import Product
from apitest.models import ApiTest, Apis


# Register your models here.


class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimetod', 'apiresult', 'apistatus', 'create_time', 'id',
                    'product']
    model = Apis
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'create_time', 'id']
    inlines = [ApisAdmin]


admin.site.register(Product)  # 把产品模块注册到Django后台并显示
