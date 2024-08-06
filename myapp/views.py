from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    top_pro=Top_Product.objects.all()
    return render(request,'index.html',{'top_pro':top_pro})

def login(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        pass1=request.POST['pass1']
        
        s=auth.authenticate(username=uname,password=pass1)
        if s is not None:
            auth.login(request,s)
            messages.success(request,'Login successful')
            return redirect('/')
        else:
            messages.error(request,'Invalid Credential!')
            
            return redirect('/login/')
        
    return render(request,'login.html')


def shop(request):
    pro=Product.objects.all()
    return render(request,'shop.html',{'pro':pro})

@login_required(login_url='/login/')
def wishlist(request):
    data=Wishlist.objects.filter(u_id=request.user)
    return render(request,'wishlist.html',{'data':data})

@login_required(login_url='/login/')
def checkout(request):
    if request.method =='POST':
        n=request.POST['name']    
        e=request.POST['email']    
        phone=request.POST['phone']    
        add=request.POST['address']    
        city=request.POST['city']    
        st=request.POST['state']    
        zip=request.POST['zip']    
        amt=request.POST['amount']    
        pay=request.POST['payment']
        id=O_tracker.objects.get(otid=1)
        s=Order(name=n,email=e,phone=phone,address=add,city=city,state=st,zip=zip,amount=amt,pay_type=pay,u_id=request.user,ot_id=id)    
        s.save()
        lastOrder=Order.objects.last()
        data=Cart.objects.filter(u_id=request.user)
        for c in data:
            p=Product.objects.get(pid=c.p_id.pid)
        
            item=O_item(o_itemid=lastOrder,p_id=p,quantity=c.quantity,sub_total=c.total())
            item.save()
            c.delete()
        return redirect('/confirmorder/'+ str(s.o_id))
    return render(request,'checkout.html')

def orderhistory(request):
    data=Order.objects.filter(u_id=request.user)
    return render(request,'orderhistory.html',{'data':data})







@login_required(login_url='/login/')
def confirmorder(request,id):
    odr=Order.objects.get(o_id=id)
    items=O_item.objects.filter(o_itemid=id)
    return render(request,'confirmorder.html',{'order_data':odr,'order_item_data':items})













@login_required(login_url='/login/')
def addtowishlist(request,id):
    data=Wishlist.objects.filter(u_id=request.user,p_id=id)
    if data:
        messages.warning(request,'Product is already added to wishlist')
        return redirect('/wishlist/')
    else:
        p=Product.objects.get(pid=id)
        s=Wishlist(p_id=p,u_id=request.user)
        s.save()
        messages.success(request,'Product added to the wishlist')
        return redirect('/wishlist/')

def deletewish(request,id):
    data=Wishlist.objects.get(u_id=request.user,wid=id)
    data.delete()
    messages.success(request,'Product deleted from wishlist')
    return redirect('/wishlist/')

def catagory(request,id):
    pro_data=Product.objects.filter(c_id=id)
    return render(request,'catagory.html',{'pro_data':pro_data})


def detail(request,id):
    pro_detail=Product.objects.get(pid=id)
    return render(request,'detail.html',{'pro_detail':pro_detail})


def register(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                messages.warning(request,'Username already exists')
                return redirect('/register/')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'Email id already exists')
                return redirect('/register/')
            else:
                s=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pass1)
                s.save()
                messages.success(request,'User id created successfully!')
                return redirect('/login/')
        else:
            messages.error(request,'Password does\'t match')
            
            return redirect('/register/')
    return render(request,'register.html')



def contact(request):
    return render(request,'contact.html')

def logout(request):
    auth.logout(request)
    messages.success(request,'Logout successfully')
    
    return render(request,'index.html')


@login_required(login_url='/login/')
def cart(request):
    data=Cart.objects.filter(u_id=request.user)
    
    return render(request,'cart.html',{'data':data})


def delete(request,id):
    data=Cart.objects.get(u_id=request.user,cid=id)
    data.delete()
    messages.success(request,'Product deleted from cart')
    return redirect('/cart/')

@login_required(login_url='/login/')
def addtocart(request,id):
    data=Cart.objects.filter(u_id=request.user,p_id=id)
    if data:
        messages.warning(request,'Product is already added to the cart')
        return redirect('/cart/')
    else:
        p=Product.objects.get(pid=id)
        s=Cart(p_id=p,u_id=request.user,quantity=1)
        s.save()
        messages.success(request,'Product added to the cart')
        return redirect('/cart/')
    
def minus(request,id):
    data=Cart.objects.get(u_id=request.user,cid=id)
    if data.quantity <=1:
        data=Cart.objects.get(u_id=request.user,cid=id)
        data.delete()
        messages.success(request,'Product deleted from cart')
        return redirect('/cart/')
    data.quantity -=1
    data.save()
    return redirect('/cart/')
    
    
def plus(request,id):
    data=Cart.objects.get(u_id=request.user,cid=id)
    
    data.quantity +=1
    if data.quantity>10:
        messages.warning(request,'Maximum quantity limit reached!!')
        return redirect('/cart/')
        
    data.save()
    return redirect('/cart/')
    
