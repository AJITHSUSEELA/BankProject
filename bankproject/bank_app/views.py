from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth import logout
# Create your views here.



def register(request):
    if request.method=='POST':
        a=registerform(request.POST,request.FILES)
        if a.is_valid():
            fn= a.cleaned_data['firstname']
            ln= a.cleaned_data['lastname']
            un= a.cleaned_data['uname']
            em= a.cleaned_data['email']
            ph= a.cleaned_data['phone']
            ac = int("15" + str(ph))
            # ac = request.POST.get('acc')
            # request.session['ac'] = ac
            im= a.cleaned_data['photo']
            pn= a.cleaned_data['pin']
            re= a.cleaned_data['repin']
            if pn==re:
                b = registermodel(firstname=fn, lastname=ln, uname=un, email=em, phone=ph, photo=im, pin=pn,balance=0,acc=ac)
                b.save()
                subject= "Your Account Has een Created"
                message= f"Your New Account Number is {ac}"
                email_from= "aneeshbank34@gmail.com"
                email_to= em
                send_mail(subject,message,email_from,[email_to])
                return redirect(login)
            else:
                return HttpResponse("Pin Doesn't Match!")
        else:
            return HttpResponse("Registration Failed!")
    return render(request,'register.html')




def login(request):
    if request.method=='POST':
        a=loginform(request.POST)
        if a.is_valid():
            un=a.cleaned_data['uname']
            pn=a.cleaned_data['pin']
            b=registermodel.objects.all()
            for i in b:
                if i.uname==un and i.pin==pn:
                    request.session['id']=i.id
                    return redirect(profile)
            else:
                    return HttpResponse("Login Failed!!")
    return render(request,'login.html')


def profile(request):
    try:
        id1=request.session['id']
        a=registermodel.objects.get(id=id1)
        img=str(a.photo).split('/')[-1]
        return render(request,'profile.html',{'a':a, 'img':img})
    except:
        return redirect(login)


def edit(request,id):
    a=registermodel.objects.get(id=id)
    if request.method=='POST':
        a.firstname=request.POST.get('firstname')
        a.lastname=request.POST.get('lastname')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        a.save()
        return redirect(profile)
    return render(request,'edit.html',{'a':a})


def imgedit(request,id):
    a=registermodel.objects.get(id=id)
    img = str(a.photo).split('/')[-1]
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(a.photo) > 0:
                os.remove(a.photo.path)
            a.photo = request.FILES['photo']
        a.uname=request.POST.get('uname')
        a.save()
        return redirect(profile)
    return render(request, 'imgedit.html', {'a': a, 'img': img})


def addamount1(request,id):
    a=registermodel.objects.get(id=id)
    if request.method=='POST':
        am=request.POST.get('amount')
        pin = request.POST.get('pin')
        request.session['am']=am #global
        request.session['ac']= a.acc
        if int(pin) == a.pin:
          a.balance+=int(am)
          a.save()
          b=addamount(amount=am,uid=request.session['id'])
          b.save()

          return redirect(success)
        else:
            return HttpResponse('Failed To Add Amount')

    return render(request,'addamount.html')


def success(request):
    am= request.session['am']
    ac= request.session['ac']
    return render(request,'success.html',{'am':am, 'ac':ac})


def withdraw(request,id):
    a=registermodel.objects.get(id=id)
    if request.method=='POST':
        am=request.POST.get('amount')
        pin = request.POST.get('pin')
        request.session['am'] = am  # global
        request.session['ac'] = a.acc
        if int(pin) == a.pin:
          if (int(am)<=int(a.balance)):
            a.balance-=int(am)
            a.save()
            b = withdrawamount(amount=am, uid=request.session['id'])
            b.save()

            return redirect(success2)
          else:
            return HttpResponse("Sorry Low Balance")
        else:
            return HttpResponse("Amount Withdraw Failed")
    return render(request,'withdraw.html')


def success2(request):
    am= request.session['am']
    ac= request.session['ac']
    return render(request,'success2.html',{'am':am, 'ac':ac})

def balance(request,id):
    a=registermodel.objects.get(id=id)
    if request.method=='POST':
        pin=request.POST.get('pin')
        request.session['ac'] = a.acc
        request.session['bl']=a.balance
        if int(pin)==a.pin:
            return redirect(success3)
        else:
            return HttpResponse("Wrong Pin")
    return render(request,'balance.html')

def success3(request):
    ac= request.session['ac']
    bl= request.session['bl']
    return render(request,'success3.html',{'ac':ac, 'bl':bl})

def mini(request,id):
    a=registermodel.objects.get(id=id)
    pin = request.POST.get('pin')
    if request.method=='POST':
        if int(pin)==int(a.pin):
            wi=request.POST.get('statement')
            if wi=="deposit":
                return redirect(depdisplay)
            elif wi=="withdraw":
                return redirect(withdisplay)
        else:
            return HttpResponse("Incorrect Password")
    return render(request,'mini.html')

def depdisplay(request):
    b=addamount.objects.all()
    id = request.session['id']
    return render(request,'depdisplay.html',{'b':b, 'id':id})

def withdisplay(request):
    a=withdrawamount.objects.all()
    id=request.session['id']
    return render(request,'withdisplay.html',{'a':a, 'id':id})

def adminhtml(request):
    if request.method=='POST':
        a=adminform(request.POST,request.FILES)
        if a.is_valid():
            top=a.cleaned_data['topic']
            cont=a.cleaned_data['content']
            b=adminmodel(topic=top,content=cont)
            b.save()
            return redirect(newsdisplay)
        else:
            return HttpResponse("Sorry Not Able To Add")
    return render(request,'adminhtml.html')


def adminlogin(request):
    if request.method=='POST':
        a=adminlogform(request.POST)
        if a.is_valid():
            us = a.cleaned_data['username']
            ps= a.cleaned_data['password']
            user= authenticate(request, username=us, password=ps)
            if user is not None:
                return redirect(adminprofile)
            else:
                return HttpResponse("Login Failed")
    return render(request,'adminlogin.html')

def adminprofile(request):
    return render(request,'adminprofile.html')

def newsdisplay(request):
    a=adminmodel.objects.all()
    id1=[]
    tp=[]
    co=[]
    dt=[]
    for i in a:
        id=i.id
        id1.append(id)
        top=i.topic
        tp.append(top)
        con=i.content
        co.append(con)
        date=i.date
        dt.append(date)
    pair=zip(tp,co,dt,id1)
    return render(request,'newsdisplay.html',{'a':pair})

def admnewsdisp(request):
    a = adminmodel.objects.all()
    id1=[]
    tp = []
    co = []
    dt = []
    for i in a:
        id=i.id
        id1.append(id)
        top = i.topic
        tp.append(top)
        con = i.content
        co.append(con)
        date = i.date
        dt.append(date)
    pair = zip(tp, co, dt,id1)
    return render(request,'admnewsdisp.html',{'a':pair})

def newsdelete(request,id):
    a=adminmodel.objects.get(id=id)
    a.delete()
    return redirect(admnewsdisp)

def newsedit(request,id):
    a=adminmodel.objects.get(id=id)
    if request.method=='POST':
        a.topic=request.POST.get('topic')
        a.content=request.POST.get('content')
        a.save()
        return redirect(admnewsdisp)
    return render(request,'newsedit.html',{'a':a})


def wish(request,id):
    a=adminmodel.objects.get(id=id)
    a1=wishlist.objects.all()
    for i in a1:
        if i.newsid==a.id and i.Uid==request.session['id']:
            return HttpResponse('Item Already in Wishlist')
    b=wishlist(topic=a.topic,content=a.content,date=a.date,newsid=a.id,Uid=request.session['id'])
    b.save()
    return HttpResponse("Added To Wishlist")

def wishmodeldisp(request):
    a=wishlist.objects.all()
    tp = []
    co = []
    dt = []
    for i in a:
        top = i.topic
        tp.append(top)
        con = i.content
        co.append(con)
        date = i.date
        dt.append(date)
    pair = zip(tp, co, dt)
    return render(request, 'wishmodeldisp.html', {'a': pair})


def logout_view(request):
    logout(request)
    return redirect(login)



def forget_password(request):
    a=registermodel.objects.all()
    if request.method=='POST':
        em= request.POST.get('email')
        ac= request.POST.get('acc')
        for i in a:
            if(i.email==em and i.acc==int(ac)):
                id=i.id
                subject="Password Change"
                message=f"http://127.0.0.1:8000/bank_app/change/{id}"
                frm="aneeshbank34@gmail.com"
                to=em
                send_mail(subject,message,frm,[to])
                return HttpResponse("Check Your E-mail")
        else:
            return HttpResponse("Sorry, Some Error Occured")
    return render(request,'forget password.html')




def change(request,id):
    a= registermodel.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('pin')
        p2=request.POST.get('repin')
        if p1==p2:
            a.pin=p1
            a.save()
            return HttpResponse("Password Changed")
        else:
            return HttpResponse("Sorry! Error Occured")
    return render(request,'change.html')



def moneytransfer(request,id):
    a= registermodel.objects.get(id=id)
    b=registermodel.objects.all()
    if request.method=='POST':
        nm= request.POST.get('name')
        ac= request.POST.get('acc')
        am= request.POST.get('amount')
        for i in b:
            if int(ac)==i.acc and nm==i.uname: #i :receive
                if a.balance>=int(am):
                    a.balance-=int(am)
                    i.balance+=int(am)
                    i.save()
                    a.save()
                    return HttpResponse("money transfered successfully")
                else:
                    return HttpResponse("insufficient balance")
        else:
                return HttpResponse("user not found")


    return render(request,'moneytransfer.html')





 # id1=[]
 #    pname=[]
 #    pr=[]
 #    desc=[]
 #    pimg=[]
 #    for i in a:
 #        id=i.id
 #        id1.append(id)
 #        pn=i.proname
 #        pname.append(pn)
 #        pri=i.price
 #        pr.append(pri)
 #        des=i.description
 #        desc.append(des)
 #        pi=str(i.proimage).split('/')[-1]
 #        pimg.append(pi)
 #    pair=zip(pname,pr,desc,pimg,id1)


# def carddelete(request,id):
#     a=cardmodel.objects.get(id=id)
#     os.remove(str(a.proimage))
#     a.delete()
#     return redirect(carddisplay)
#
# def cardedit(request,id):
#     a=cardmodel.objects.get(id=id)
#     img=str(a.proimage).split('/')[-1]
#     if request.method=='POST':
#         a.proname=request.POST.get('proname')
#         a.price=request.POST.get('price')
#         a.description=request.POST.get('description')
#         if len(request.FILES)!=0:
#             if len(a.proimage)!=0:
#                 os.remove(a.proimage.path)
#             a.proimage=request.FILES['proimage']
#         a.save()
#         return redirect(carddisplay)
#     return render(request,'cardedit.html',{'a':a,'img':img})

