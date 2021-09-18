from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse
import json as simplejson
from django.db.models import Q
# Create your views here.

def home(request):
    context= {}
    return render(request, 'dashboard.html', context)

def goodsreceived(request):
    Productobj=ProductModel.objects.all()
    Itemobj=ItemModel.objects.all()
    countries = ProductModel.objects.all()
    if request.method == 'POST':
        formset=Goods_received_noteForm(request.POST)
        if formset.is_valid():
        
            formset.save()
        else:
            print(formset.errors)
            
    formset=Goods_received_noteForm()
    context={'formset':formset, 'Productdata':Productobj, 
    'Itemdata':Itemobj, 'countries': countries}
    return render(request, 'store/create_goodsreceived.html', context)

def view_goodsreceived(request):
    Productobj=ProductModel.objects.all()
    Itemobj=ItemModel.objects.all()
    countries = ProductModel.objects.all()
    
    all_objects=Goods_received_note.objects.all()
    formset=Goods_received_noteForm()
    
    context= {'all_objects': all_objects, 'formset':formset, 'Productdata':Productobj, 
    'Itemdata':Itemobj, 'countries': countries}
    
    return render(request, 'store/view_goodsreceived.html', context)

def get_details(request):

    
    product_name = request.GET['cnt']
    print("ajax " + str(product_name))

    result_set = []
    all_items = []
    
    answer = str(product_name[1:-1])
    selected_product = ProductModel.objects.get(Pname=answer)
    lolo = selected_product.Pid
    print("selected product name " + str(selected_product))
   
    all_items = ItemModel.objects.filter(Pid=ProductModel.objects.get(pk=lolo))
    for item in all_items:
        print("item name " + str(item.Itemname))
        result_set.append({'name': item.Itemname})

    return HttpResponse(simplejson.dumps(result_set), content_type='application/json')

def create_issuereceipt(request):
    formset1=Issue_receipt_voucherForm
    context= {'formset1': formset1}
    return render(request, 'store/create_issuereceipt.html', context)

def view_issuereceipt(request):
    all_objects=Issue_receipt_voucher.objects.all()
    context={'all_objects': all_objects}
    return render(request, 'store/view_issuereceipt.html', context)

def getdetails(request):

    
    product_name = request.GET['cnt']
    print("ajax " + str(product_name))

    result_set = []
    all_items = []
    
    answer = str(product_name[1:-1])
    selected_product = ProductModel.objects.get(Pname=answer)
    lolo = selected_product.Pid
    print("selected product name " + str(selected_product))
   
    all_items = ItemModel.objects.filter(Pid=ProductModel.objects.get(pk=lolo))
    for item in all_items:
        print("item name " + str(item.Itemname))
        result_set.append({'name': item.Itemname})

    return HttpResponse(simplejson.dumps(result_set), content_type='application/json')


def search_product(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        venues= Goods_received_note.objects.filter(Q(subcategory__icontains=searched) | Q(category__contains=searched) |
                                            Q(condition__icontains=searched) | Q(date__contains=searched))
         
        context={'searched':searched, 'venues':venues}
        return render(request, 'store/search.html', context)
    else:
        context={}
        return render(request, 'store/search.html', context)

    