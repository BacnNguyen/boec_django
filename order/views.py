from django.db import reset_queries
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import redirect, render
from django.views import View
from cart.models import *
from .models import *
from user.models import *
from order.feedback_process.classify import check


# Create your views here.
class AddOrder(View):
    def post(self,request):
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            cartItem = cart.cartitem_set.all()
            total=request.POST.get('total')
            shipping_id =request.POST.get('shipping_id')
            payment_id =request.POST.get('payment_id')
            ship= Shipping.objects.get(pk = shipping_id)
            pay =Payment.objects.get(pk = payment_id)
            address_user=Address.objects.get(user= request.user,default=True)
            shipping_address = address_user.street +',' +  address_user.apartment_number+','+ address_user.district+ ','+address_user.city
            order =Order.objects.create(user=request.user,cart= cart,shipping_address=shipping_address,ship=ship, paymentMethod=pay,total=total)
            for cart_item in cartItem:
                OrderDetail.objects.create(order= order, product= cart_item.item,product_name=cart_item.item.title, image =cart_item.item.thumbnail,quantity= cart_item.quantity,price=cart_item.item.sale_price)
                # HttpResponse(item.item.sale_price)
            cart.cartitem_set.all().delete()    
            return HttpResponse(1)
class GetRatingOrder(View):
    def get(self,request):
        if request.user.is_authenticated:
            id= request.POST.get('id')
            order =Order.objects.get(pk=18, user=request.user)   
            o = list(OrderDetail.objects.filter(is_rating=True, order=order).values())
         
            comment =list(Comment.objects.filter(order_id=18).values())
        return JsonResponse({"o":o,"c":comment},safe=False)
     
    def post(self,request):
        if request.user.is_authenticated:
            id= request.POST.get('id')
            order =Order.objects.get(pk=id, user=request.user)   
            o = list(OrderDetail.objects.filter(is_rating=True, order=order).values())
         
            comment =list(Comment.objects.filter(order_id=id).values())
        return JsonResponse({"o":o,"c":comment},safe=False)

class FeedBack(View):
    def get(self,request):
        comments = Comment.objects.filter(checked = True)
        context ={}
        context['comments'] = comments
        return render(request,"order/viewfeedback.html",context)
class ViewFeedback(View):
    def get(self,request):
        comments = Comment.objects.filter(checked = True)
        context ={}
        context['comments'] = comments
        return render(request,"order/viewfeedback.html",context)
class CheckFeedback(View):
    def get(self,request):
        comments = Comment.objects.filter(checked = False)
        for cmt in comments:
            res =check(cmt.comment)
            # print(cmt.comment)
            cmt.type_comment =res 
            cmt.save()

        context ={}
        context['comments'] = comments
        return render(request,"order/checkfeedback.html",context)
class Delete_Comment(View):
    def post(self,request):
        id = request.POST.get('id_cmt')
        Comment.objects.filter(id=id).delete()
        return HttpResponse(1)

class Ignore_Comment(View):
    def post(self,request):
        id = request.POST.get('id_cmt')
        comment = Comment.objects.get(id=id)
        comment.checked = True
        comment.save()
        return HttpResponse(1)
class Reply_Comment(View):
    def post(self,request):
        id_cmt = request.POST.get('id_cmt')
        print("id comment",id_cmt)
        content_rep = request.POST.get('content_rep')
        comment=Comment.objects.get(id=id_cmt)
        comment.checked = True
        comment.save()
        rep_cmt = ReplyComment.objects.create(comment=comment,content=content_rep)
        rep_cmt.save()
        return HttpResponse(1)

class OrderManage(View):
    def get(seft,request):
        if request.user.is_authenticated:
            orders =Order.objects.all()
            context={}
            context['orders']= orders
            return render(request,"order/manage.html",context)
        else:
            return redirect('account:login')
    def post(seft,request):
        if request.user.is_authenticated:
            orders =Order.objects.all()
            context={}
            context['orders']= orders
            return render(request,"order/manage.html",context)
        else:
            return redirect('account:login')
class OrderStatus(View):
    def get(seft,request,type):
        status =type
        if status==0:
            order = Order.objects.all()
            count = order.count()
        else:
            order = Order.objects.filter(status=status)
            count = order.count()
        
       
        context={}
        context['orders']=order
        context['active'] =status    
        context['count']=count
       
        return render(request,"order/manage.html",context)
    def post(seft,request,type):
        status =type
        count={}
        if status==0:
            order = Order.objects.all()
            count = order.count()
        else:
            order = Order.objects.filter(status=status)
            count = order.count()
        

        context={}
        context['orders']=order
        context['active'] =status    
        context['count']=count
        return render(request,"order/manage.html",context)
        # return JsonResponse(order,safe=False)
class UpdateStatus(View):
    def get(seft,request,order,type):
        Order.objects.filter()
        return HttpResponse(1)
    def post(seft,request):
        order = request.POST.get('orderid')
        type = request.POST.get('type')
        type1= int(type)+1
        Order.objects.filter(pk=order,status=int(type)).update(status=type1)
        # return HttpResponse(order)
        return HttpResponseRedirect(seft.request.META.get('HTTP_REFERER'))
      