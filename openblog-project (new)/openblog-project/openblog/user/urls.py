from django.urls import path
from .views import *
urlpatterns=[
    path('userhome/',UserHome.as_view(),name="userhome"),
    path('profile/',ProfileView.as_view(),name="pro"),
    path('addprofile/',AddProfile.as_view(),name="addpro"),
    path('Cpass/',CpassView.as_view(),name="cpass"),
    path('edit/<int:pk>',EditView.as_view(),name="edit"),   
    path('myblog/',MyBlogView.as_view(),name="mblog"),
    path('editblog<int:pk>/',EditBlog.as_view(),name="editb"),
    path('delblg/<int:pk>',DeleteBlog.as_view(),name="delb"),
    path('addc/<int:bid>',commentadd,name="cmnt"),
    path('addl/<int:id>',addlike,name="addl"),
    path('likedview/',LikedView.as_view(),name="lview"),
]
