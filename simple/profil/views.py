from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import*
from django.http.response import HttpResponse
from django.contrib import messages
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request, 'home.html')

def DaftarPage(request):
    if request.method=='POST':
       uname=request.POST.get('username')
       email=request.POST.get('email')
       pass1=request.POST.get('password1')
       pass2=request.POST.get('password2')

       if pass1!=pass2:
           return HttpResponse("you password and confrom password are not same!!")
       else:    
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
       return redirect('login')
       
    return render (request, 'daftar.html')

def LoginPage(request):
    if request.method=='POST':
       username=request.POST.get('username')
       pass1=request.POST.get('pass')
       user=authenticate(request,username=username,password=pass1)
       if user is not None:
          login(request,user)
          return redirect('home')
       else:
          return HttpResponse("Username or password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def add_item(request):
   if request.method=='POST':
      name = request.POST['name']
      Description = request.POST['Description']
      item = name(name = name,Description = Description)
      item.save()
      messages.info(request,"ITEM ADDEDD SUCCESSFULLY")
   else:
      pass
   item_list = name.objects.all()
   context = {
      'item_list' : item_list
   }

   return render(request,'home.html', context)


def delete_item(request,myid):
   item = name.objects.get(id =myid)   
   item.delete()
   messages.info(request, "ITEM DELETE SUCCESSFULY")
   return redirect(HomePage)  

def edit_item(request,myid):
   sel_item = name.objects.get(id =myid)

   context ={
      'sel_item':sel_item,
   }
   return render(request, 'home.html')   