from django import forms
from account.models import UserProfile,Blogs,Comments

class ProfieForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        exclude=['user']

class CPassForm(forms.Form):
    old_pass=forms.CharField(max_length=100,label="Old Password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Old Password"}))
    new_pass=forms.CharField(max_length=100,label="New Password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter New Password"}))
    confirm_pass=forms.CharField(max_length=100,label="Confirm Password",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Re-enter New Password"}))

class BlogForm(forms.ModelForm):
    class Meta:
        model =Blogs
        fields = ["title","description","image"]
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "image":forms.FileInput(),
     }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=["comment"]
        widgets={
            "comment":forms.Textarea(attrs={"class":"form-control"})
        }