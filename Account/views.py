from django.contrib.auth.models import Group
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as logouts
from django.contrib.auth import login as logins
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from Account.models import SignUpForm
from cart.models import Cart
from user.models import Address, CustomerUser
 
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    return render(request,"homepage/home-page.html",{"user":request.user})
def register(request):
    User = get_user_model()
    print(User)
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            group = Group.objects.get(name='customer')
            user_name = form.data.get('username')
            user = User.objects.get(username=user_name)
            user.groups.add(group)
            customer = CustomerUser.objects.all()
            for c in customer:
                # create new cart for user
                if user_name is c.username:
                    cart = Cart(CustomerUser__id=c.id)
                    cart.save()
                    break

            return redirect("account:login")
    else:
        form =SignUpForm()
    return render(request,"Account/register.html",{"form":form})

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
            if user is None:
                return HttpResponse("Tai khoan khong ton tai")
            logins(request,user)
          
            if 'kho' in user.get_username():
                return redirect('nhaphang:kho')
            id_user = user.id
            cart = Cart.objects.filter(user=CustomerUser.objects.get(id=id_user)).exists()
            address = Address.objects.filter(user=CustomerUser.objects.get(id=id_user)).exists()
            if not cart:
                new_cart= Cart.objects.create(user=CustomerUser.objects.get(id=id_user))
                new_cart.save()
            if not address:
                new_address = Address.objects.create(user=CustomerUser.objects.get(id=id_user))
                new_address.save()
            return redirect('account:home')
    else:
        form=AuthenticationForm() 
    return render(request,"Account/login.html",{"form":form})

def logout(request):
    logouts(request)
    return redirect('/')