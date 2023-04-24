from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,CreateView,FormView,UpdateView,DeleteView
from .forms import *
from account .models import UserProfile,Blogs,Comments
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.http import HttpResponse
# Create your views here.
# class UserHome(TemplateView):
#     template_name="userhome.html"

class UserHome(CreateView):
    form_class=BlogForm
    model=Blogs
    template_name="userhome.html"
    success_url=reverse_lazy("userhome")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.objects=form.save()
        messages.success(self.request,"Blog Posted!!")
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Blogs.objects.all().order_by("-date")
        context["cform"]=CommentForm()
        context["comments"]=Comments.objects.all()
        print(context["data"])
        return context
def commentadd(request,*args,**kwargs):
    if request.method=="POST":
        bid=kwargs.get("bid")
        blog=Blogs.objects.get(id=bid)
        cmnt=request.POST.get("comment")
        user=request.user
        Comments.objects.create(comment=cmnt,user=user,blog=blog)
        messages.success(request,"Comment Submitted!!")
        return redirect("userhome")
    
def addlike(request,*args,**kwargs):
    bid=kwargs.get("id")
    blog=Blogs.objects.get(id=bid)
    blog.liked_by.add(request.user)
    blog.save()
    return redirect("userhome")

class ProfileView(TemplateView):
    template_name="profile.html"  

class AddProfile(CreateView):
    template_name="addprofile.html"
    form_class=ProfieForm
    model=UserProfile
    success_url=reverse_lazy("pro")
    def form_valid(self,form):
        form.instance.user=self.request.user
        self.objects=form.save()
        messages.success(self.request,"Profile Added!!")
        return super().form_valid(form)
    
class CpassView(FormView):
    template_name="cpass.html"
    form_class=CPassForm
    def post(self,request,*args,**kwargs):
        form=self.form_class(data=request.POST)
        if form.is_valid():
            old=form.cleaned_data.get("old_pass")
            new=form.cleaned_data.get("new_pass")
            cnf=form.cleaned_data.get("confirm_pass")
            user=authenticate(request,username=request.user.username,password=old)
            if user:
                if new==cnf:
                    # user.password=new
                    user.set_password(new)
                    user.save()
                    logout(request)
                    messages.success(request,"Password Changed")
                    return redirect("log")
                else:
                    messages.error(request,"Passwords mismached")
                    return  redirect("cpass")
            else:
                messages.error(request,"Old password entered is incorrect!!")
                return redirect("cpass")

class EditView(UpdateView):
    form_class=ProfieForm
    model=UserProfile
    success_url=reverse_lazy("pro")
    template_name="edit.html"
    pk_url_kwargs="pk"
    def form_valid(self,form):
        messages.success(self.request,"Profile Updated")
        self.object=form.save()
        return super().form_valid(form)
    #     pid=kwargs.get("pid")
    #     p=UserProfile.objects.get(id=pid)
    #     f=ProfieForm(instance=p)
    #     return render(request,"edit.html",{"form":f})
    # def post(self,request,*args,**kwargs):
    #     pid=kwargs.get("pid")
    #     p=UserProfile.objects.get(id=pid)
    #     form_data=ProfieForm(data=request.POST,files=request.FILES,instance=p)
    #     if form_data.is_valid():
    #         form_data.save()
            # messages.success(self,request,"Profile Updated")
    #         return redirect("pro")
    #     else:
    #         return render(request,"edit.html",{"form":form_data})


class MyBlogView(TemplateView):
    template_name="myblog.html"  
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Blogs.objects.filter(user=self.request.user).order_by('-date')
        return context

# class EditBlogView(UpdateView):
#     form_class=ProfieForm
#     model=UserProfile
#     success_url=reverse_lazy("editblog")
#     template_name="edit.html"
#     pk_url_kwargs="pk"
#     def form_valid(self,form):
#         messages.success(self.request,"Profile Updated")
#         self.object=form.save()
#         return super().form_valid(form)
 
class DeleteBlog(DeleteView):
    model=Blogs
    success_url=reverse_lazy("mblog")
    template_name="deleteblog.html"
   

class EditBlog(UpdateView):
    form_class=BlogForm
    model=Blogs
    success_url=reverse_lazy("mblog")
    template_name="editblog.html"
    pk_url_kwargs="pk"
    def form_valid(self,form):
        messages.success(self.request,"Blog Updated")
        self.object=form.save()
        return super().form_valid(form)
                
class LikedView(TemplateView):
    template_name="likedview.html"  