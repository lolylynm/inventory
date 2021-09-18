from .models import *
from django import forms
from django.forms import formset_factory
from django.forms import modelformset_factory
from functools import partial
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit




class Goods_received_noteForm(forms.ModelForm):

    condition_choices = [
            ('Fair', 'Fair'),
            ('new', 'new'),
            ('old', 'old'),
        ]


    customer=forms.CharField(label='Customer', max_length=300)
    date= forms.DateField(widget=forms.TextInput(attrs={'readonly':'readonly'}),label='Date',
             initial=datetime.datetime.now())

    serial_number = forms.CharField(max_length=400, label='Serial Number')
    category = forms.CharField(label='category')
    subcategory = forms.CharField( max_length=400, label='subcategory')
    condition = forms.ChoiceField(choices=condition_choices, label='condition')

    quantity = forms.IntegerField(label='Quantity')
    description = forms.CharField(label='Description', max_length=300)
    order_no = forms.CharField(label='Order No.', max_length=200)
    stores_no = forms.CharField(label='Stores No', max_length=300)
    unit_cost=forms.CharField(label='Unit Cost', max_length=300)

    comments = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}), max_length=1000, label='Comments')

    ordered_by=forms.CharField(label='Ordered By', max_length=300)
    received_by=forms.CharField(label='Received By', max_length=300)
    checked_by = forms.CharField(label='Checked by', max_length=300)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-sm-9'
        self.helper.label_class = 'col-sm-3' 
        self.helper.layout = Layout(
            Fieldset(
                'customer',
                
            ),
        )

    class Meta:
            model = Goods_received_note
            fields = '__all__'

Goods_received_noteFormSet = modelformset_factory(Goods_received_note, exclude=(), form=Goods_received_noteForm)
formset = Goods_received_noteFormSet(queryset=Goods_received_note.objects.all())


class Issue_receipt_voucherForm(forms.ModelForm):
    site_name=forms.CharField(label='Site Name', max_length=300)
    date= forms.DateField(widget=forms.TextInput(attrs={'readonly':'readonly'}),label='Date',
             initial=datetime.datetime.now())

    stores_request_no = forms.CharField(label='Stores Req. No', max_length=300)
    request_description = forms.CharField(label='Request Description', max_length=300)
    unit=forms.CharField(label='Unit', max_length=300)
    quantity = forms.IntegerField(label='Quantity')

    issued_by=forms.CharField(label='Issued By', max_length=300)
    issuere_title=forms.CharField(label='Issuer Title', max_length=300)
    approved_by=forms.CharField(label='Approved By', max_length=300)
    approver_title=forms.CharField(label='Approver Title', max_length=300)
    ferried_by = forms.CharField(label='Ferried by', max_length=300)
    ferrier_title=forms.CharField(label='Ferrier Title', max_length=300)
    received_by=forms.CharField(label='Received By', max_length=300)
    receiver_title=forms.CharField(label='Receiver Title', max_length=300)
    stock_entered_by=forms.CharField(label='Stock Entered By', max_length=300)
    stock_enterer_title=forms.CharField(label='Stock Enterer Title', max_length=300)

    destination = forms.CharField(label='Destination', max_length=300)
    comments=forms.CharField(label='Comments', max_length=300)

    class Meta:
            model = Issue_receipt_voucher
            fields = '__all__'