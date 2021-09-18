from django.contrib import admin
from .models import *
from .views import *





# Register your models here.

admin.site.register(Goods_received_note)
admin.site.register(Issue_receipt_voucher)

class ProductModel_Admin(admin.ModelAdmin):
    list_display = ('Pid' ,'Pname')

admin.site.register(ProductModel, ProductModel_Admin)


class ItemModel_Admin(admin.ModelAdmin):
    list_display = ('Pid', 'Itemid','Itemname')
admin.site.register(ItemModel, ItemModel_Admin)