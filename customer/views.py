from django.shortcuts import render,redirect
from customer.forms import Registrationform,Loginform
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from store.models import Products,Carts,Orders

# Create your views here.
class SignupView(View):
    def get(self,request,*args,**kwargs):
        form=Registrationform()
        return render(request,"signup.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=Registrationform(request.POST)
        if form.is_valid():
            form.save()
            print("inside save")
            return redirect("signin")
        else:
            print("outside save")
            return render(request,"signup.html",{"form":form})

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=Loginform()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=Loginform(request.POST)
        if form.is_valid():
            unm=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(unm,pwd)
            usr=authenticate(request,username=unm,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                return render(request,"login.html",{"form":form})

class HomeView(View):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        return render(request,"home.html",{"products":qs})

class ProductDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Products.objects.get(id=id)
        return render(request,"product-detail.html",{"product":qs})

class AddtocartView(View):
    def post(self,request,*args,**kwargs):
        qty=request.POST.get("qty")
        user=request.user
        id=kwargs.get("id")
        product=Products.objects.get(id=id)
        Carts.objects.create(product=product,user=user,qty=qty)
        return redirect("home")

class CartListView(View):
    def get(self,request,*args,**kwargs):
        qs=Carts.objects.filter(user=request.user,status="in-cart")
        return render(request,"cart-list.html",{"carts":qs})

class CartRemoveview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Carts.objects.filter(id=id).update(status="cancelled")
        return redirect("home")
        
class MakeOrderView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Carts.objects.get(id=id)
        return render(request,"checkout.html",{"cart":qs})
    def post(self,request,*args,**kwargs):
        user=request.user
        address=request.POST.get("address")
        id=kwargs.get("id")
        cart=Carts.objects.get(id=id)
        product=cart.product
        Orders.objects.create(product=product,user=user,address=address)
        cart.status="order-placed"
        cart.save()
        return redirect("home")

class OrderView(View):
    def get(self,request,*args,**kwargs):
        qs=Carts.objects.filter(user=request.user,status="order-placed")
        return render(request,"order-list.html",{"order":qs})


