from django.db import models
import datetime
 
# Create your models here.

class ProductModel(models.Model):
    Pid=models.CharField(primary_key=True, max_length=200)
    Pname=models.CharField(max_length=200)
    class Meta:
        db_table="Producttable"
    def __str__(self):
        return self.Pname

class ItemModel(models.Model):
    Itemid=models.CharField(primary_key=True, max_length=200)
    Itemname=models.CharField(max_length=200)
    Pid=models.ForeignKey('ProductModel', on_delete = models.CASCADE,)
    class Meta:
        db_table="Itemstable"
    def __str__(self):
        return self.Itemname

class Goods_received_note(models.Model):
    condition_choices = [
        ('Fair', 'Fair'),
        ('new', 'new'),
        ('old', 'old')
    ]

    customer=models.CharField(max_length=300, default="Customer Name")
    date= models.DateField(default=datetime.datetime.now())

    serial_number = models.CharField( max_length=400, default="Serial Number")
    category = models.CharField( max_length=400, default="category")
    subcategory = models.CharField( max_length=400, default="subcategory")
    condition = models.CharField( max_length=400, default="condition", choices=condition_choices)
    comments = models.TextField( max_length=400, default="comment")

    quantity = models.IntegerField(default="Quantity")
    description = models.CharField(max_length=300, default="Description")
    order_no = models.CharField(max_length=200, default="Order No.")
    stores_no = models.CharField(max_length=300, default="Stores No")
    unit_cost=models.CharField(max_length=300, default="Unit Cost'")

    ordered_by=models.CharField(max_length=300, default="Ordered By")
    received_by=models.CharField(max_length=300, default="Received By")
    checked_by = models.CharField(max_length=300, default="Checked by")

    issued = models.IntegerField(default="0")
    def __str__(self):
        return self.customer

class Issue_receipt_voucher(models.Model):
    
    id1=models.ForeignKey('Goods_received_note', on_delete = models.CASCADE,null=True)
    site_name=models.CharField(max_length=300, default="Site Name")
    date= models.DateField(default=datetime.datetime.now())

    stores_request_no = models.CharField(max_length=300, default="Stores Req. No")
    quantity = models.IntegerField(default="Quantity")

    issued_by=models.CharField(max_length=300, default="Issued By")
    issuere_title=models.CharField(max_length=300, default="Issuer Title")
    approved_by=models.CharField(max_length=300, default="Approved By")
    approver_title=models.CharField(max_length=300, default="Approver Title")
    ferried_by = models.CharField(max_length=300, default="Ferried by")
    ferrier_title=models.CharField(max_length=300, default="Ferrier Title")
    received_by=models.CharField(max_length=300, default="Received By")
    receiver_title=models.CharField(max_length=300, default="Receiver Title")
    stock_entered_by=models.CharField(max_length=300, default="Stock Entered By")
    stock_enterer_title=models.CharField(max_length=300, default="Stock Enterer Title")

    destination = models.CharField(max_length=300, default="Destination")
    comments=models.TextField(max_length=300, default="Comments")

    condition_choices = [
        ('Fair', 'Fair'),
        ('new', 'new'),
        ('old', 'old')
    ]

    customer1=models.CharField(max_length=300, default="Customer Name")
    date1= models.DateField(default=datetime.datetime.now())

    serial_number1 = models.CharField( max_length=400, default="Serial Number")
    category1 = models.CharField( max_length=400, default="category")
    subcategory1 = models.CharField( max_length=400, default="subcategory")
    condition1 = models.CharField( max_length=400, default="condition", choices=condition_choices)
    comments1 = models.TextField( max_length=400, default="comment")

    quantity1 = models.IntegerField(default="Quantity")
    description1 = models.CharField(max_length=300, default="Description")
    order_no1 = models.CharField(max_length=200, default="Order No.")
    stores_no1 = models.CharField(max_length=300, default="Stores No")
    unit_cost1=models.CharField(max_length=300, default="Unit Cost'")

    ordered_by1=models.CharField(max_length=300, default="Ordered By")
    received_by1=models.CharField(max_length=300, default="Received By")
    checked_by1= models.CharField(max_length=300, default="Checked by")

    def __str__(self):
        return self.site_name 