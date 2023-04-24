from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,FormView
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
class HomeView(TemplateView):
    template_name="main_home.html"
class RegView(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=User
    success_url=reverse_lazy('h')
# class RegView(View):
#     def get(self,request,*args,**kwargs):
#         f=RegForm()
#         return render(request,"reg.html",{"form":f})
#     def post(self,request,*args,**kwargs):
#         form_data=RegForm(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"User Registered Successfully")
#             return redirect("h")
#         else:
#             messages.error(request,"User Registered failed")  
#             return render(request,"reg.html",{"form":form_data})  

# class LogView(View):
#     def get(self,req,*args,**kwargs):
#         f=LogForm()
#         return render(req,"log.html",{"form":f})
#     def post(self,request,*args,**kwargs):
#         form_data=LogForm(data=request.POST)
#         if form_data.is_valid():
#             un=form_data.cleaned_data.get("uname")
#             ps=form_data.cleaned_data.get("psw")
#             user=authenticate(request,username=un,password=ps)
#             if user:
#                 login(request,user)
#                 messages.success(request,"Login successfully")
#                 return redirect("userhome")
#             else:
#                 messages.error(request,"Login failed")
#                 return redirect("log")
#         else:
#             return render(request,"log.html",{"form":form_data}) 
class LogView(FormView):
    form_class=LogForm
    template_name="log.html"
    def post(self,request,*args,**kwargs):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
            un=form_data.cleaned_data.get("uname")
            ps=form_data.cleaned_data.get("psw")
            user=authenticate(request,username=un,password=ps)
            if user:
                login(request,user)
                messages.success(request,"Login successfully")
                return redirect("userhome")
            else:
                messages.error(request,"Login failed")
                return redirect("log")
        else:
            return render(request,"log.html",{"form":form_data}) 
        
class LogOutView(CreateView):
    def get(self,request):
        logout(request)
        return redirect("log")