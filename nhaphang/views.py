from typing import Text
from django.db import reset_queries
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
# from product import models
from product.models import Category, Product
from django.core.paginator import Paginator
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    
    context={}
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 12) # Show 25 contacts per page.
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    for item in page_obj:
        item.sale_price ="₫{:,.0f}".format(item.sale_price)
    context['page_obj']= page_obj
    # return render(request, 'product/product.html', context)
    return render(request,"nhaphang/xemsanpham.html",context)
def xemsanpham(request):
    context={}
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 12) # Show 25 contacts per page.
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    for item in page_obj:
        item.sale_price ="₫{:,.0f}".format(item.sale_price)
    context['page_obj']= page_obj
    # return render(request, 'product/product.html', context)
    return render(request,"nhaphang/xemsanpham.html",context)

def nhaphang(request):
    context ={}
    if request.method =='POST':
        category = request.POST['category']
        print('title:',category)
        pname = request.POST['pname']
        price = request.POST['price']
        description = request.POST['description']
        number = request.POST['number']
        active = False
        cate_instance = Category.objects.get(title = category)
        print("cate ins:",cate_instance)
        obj = Product.objects.create(
            title =pname,
            desc = description,
            category = cate_instance,
            price = int(price),
            sale_price = int(price),
            inventory = int(number),
            thumbnail = "",
            active = active
        )
        obj.save()
    
    list_category = Category.objects.all()
    context['cate'] = list_category
    
    return render(request,"nhaphang/nhaphang.html",context)

def search(request):
    print("Searching....")
    context={}
    text = request.GET.get('q')
    print(text)
    if text:
        print("Filer......")
        product_list = Product.objects.filter(title__icontains=text)
    else:
        print("All----------")
        product_list = Product.objects.all()
    paginator = Paginator(product_list, 12) # Show 25 contacts per page.
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for item in page_obj:
            item.sale_price ="₫{:,.0f}".format(item.sale_price)
    context['page_obj']= page_obj

    if request.is_ajax():
        print("Ajax======================")
        html = render_to_string(
            template_name="nhaphang/result_product.html", 
            context={'page_obj': page_obj}
        )

        data_dict = {'html_from_view': html}

        return JsonResponse(data=data_dict, safe=False)
    return render(request,"nhaphang/xemsanpham.html",context)