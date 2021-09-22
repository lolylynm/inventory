from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
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

def create_issuereceipt(request):
    formset1=Issue_receipt_voucherForm
    all_objects=Goods_received_note.objects.filter(issued=1)
    context= {'formset1': formset1, 'all_objects':all_objects}
    return render(request, 'store/create_issuereceipt.html', context)

def search_issuereceipt(request):
    all_objects=Goods_received_note.objects.filter(issued=0)
    context={'all_objects': all_objects}
    return render(request, 'store/search_issuereceipt.html', context)

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

def assign_html(request, pk):
    news = get_object_or_404(Goods_received_note, id=pk)
    formset2=Issue_receipt_voucherForm(request.POST)
    if request.method == 'POST':
        if formset2.is_valid():
            formset1 = formset2.save(commit=False)
            # issue = Goods_received_note.objects.get(id=pk)
            formset1.customer1 = news.customer
            formset1.date1 = news.date
            formset1.serial_number1 = news.serial_number
            formset1.category1 = news.category
            formset1.subcategory1 = news.subcategory
            formset1.condition1 = news.condition
            formset1.comments1 = news.comments
            formset1.quantity1 = news.quantity
            formset1.description1 = news.description
            formset1.order_no1 = news.order_no
            formset1.stores_no1 = news.stores_no
            formset1.unit_cost1 = news.unit_cost
            formset1.received_by1 = news.received_by
            formset1.ordered_by1 = news.ordered_by
            formset1.checked_by1 = news.checked_by
            if news.issued == 0:
                news.issued = 1
                news.save()

            formset1.save()

            print(formset1.subcategory1)
            print(formset1.category1)

            # new_form = formset1.save(commit=False)
            # new_form.save()
        else:
            print(formset2.errors)
    
    formset2=Issue_receipt_voucherForm()

    context={'news':news,'formset1':formset2}
    return render(request, 'store/assign.html', context)

from django.http import HttpResponse
from inventory_system.utils import html_to_pdf_directly

def print_check(request):
    dict = {}
    data={}
    some_var = request.POST.getlist('checks')
    print(some_var)

    for x in some_var:
        lol=Goods_received_note.objects.get(id=int(x))
        dict[x]=lol
    print(dict)
    data['data']=dict
    pdf = html_to_pdf_directly('store/goodsreceived_print.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def issueprint_check(request):
    dict = {}
    data={}
    some_var = request.POST.getlist('checks')
    print(some_var)

    for x in some_var:
        lol=Issue_receipt_voucher.objects.filter(id=int(x))
        dict[x]=lol
    print(dict)
    data['data']=dict
    pdf = html_to_pdf_directly('store/issuereceipt_print.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

    