from order.models import Order
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from user.models import Comment,Address
from product.models import Product
from order.models import *

# Create your views here.


class OrderPurchase(View):
    def get(seft, request):
        if request.user.is_authenticated:
            context={}
            detail =[]
            order =Order.objects.filter(user=request.user)
            context['order'] = order
           
            # return HttpResponse(detail)
            return render(request,"user/purchase.html",context)

class AddressView(View):
    def get(seft,request):
      
        context={}
        addresses = Address.objects.filter(user=request.user)
        for add in addresses:
            add.address = add.ToString()
        context['address'] =addresses
      
        # return HttpResponse(addresses)
        return render(request,"user/address.html",context)
    def post(seft,request):
        address_id = request.POST.get('address_id')
        Address.objects.filter(user=request.user,default=True).update(default=False)
        Address.objects.filter(pk=address_id).update(default=True)
       
        return HttpResponse(1 ,"user:address")
class Add_Address(View):
    def post(seft,request):
        reciever = request.POST.get('reciever')
        phone_reciever = request.POST.get('phone_reciever')
        street =request.POST.get('street')
        apartment =request.POST.get('apartment')
        district =request.POST.get('district')
        city =request.POST.get('city')
        Address.objects.create(user= request.user,reciever= reciever,phone_reciever=phone_reciever, street= street,apartment_number= apartment,district=district,city=city)
        return HttpResponse(1)
class Edit_Address(View):
    def post(seft,request):
        id= request.POST.get('id')
        fullname =request.POST.get('reciever')
        print('fullname:',fullname)
        phone =request.POST.get('phone')
        street =request.POST.get('street')
        apartment =request.POST.get('apartment')
        print('apartment:',apartment)
        district =request.POST.get('district')
        city =request.POST.get('city')
        add =Address.objects.get(pk=id)
        add.reciever = fullname
        add.phone_reciever = phone
        add.street =street
        add.apartment_number=apartment
        add.district =district
        add.city=city
        add.save()
        print('edited.')
        return HttpResponse(1)
class Delete_Address(View):
    def post(seft,request):
        id= request.POST.get('id')
        add =Address.objects.get(pk=id)
        add.delete()
        return redirect("user:address")
        
class CommentProduct(View):
    def post(seft,request):
        if request.user.is_authenticated:
            product_id =request.POST.get('id_pro')
            order_id =request.POST.get('id_order')
            score =request.POST.get('score')
            comment =request.POST.get('comment')
            pro = Product.objects.get(id= product_id)

          
            Comment.objects.create(user = request.user, product=pro,comment=comment,rating=int(score),order_id=int(order_id))
            OrderDetail.objects.filter(order =Order.objects.get(pk=order_id),product=pro).update(is_rating=True)
            return HttpResponse(pro)
        # return HttpResponse(1)
        
class change_default_address(View):
    def post(self,request):
        id_address = request.POST.get('id_address')
        print(id_address)
        all_address = Address.objects.filter(user=request.user)
        for add in all_address:
            print(add.id)
            if int(add.id) == int(id_address):
                print("Changed")
                add.default = True
                add.save()
            else:
                add.default = False
                add.save()
        return  HttpResponse(1 ,"cart:checkout")