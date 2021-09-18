"""inventory_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  path
from . import views
from django.conf.urls import url

urlpatterns = [
    # path('', admin.site.urls),
    path('', views.home, name='home'),
    path('goodsreceived', views.goodsreceived, name='goodsreceived'),
    path('view_goodsreceived', views.view_goodsreceived, name='view_goodsreceived'),
    path('create_issuereceipt', views.create_issuereceipt, name='create_issuereceipt'),
    path('view_issuereceipt', views.view_issuereceipt, name='view_issuereceipt'),
    url(r'^getdetails/', views.getdetails),
    url(r'^get_details/', views.getdetails),
    path('search_product', views.search_product, name='search_product'),
]
