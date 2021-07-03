from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='blog-home'),
    path('about/', views.about,name='blog-about'),
    path('signin/', views.signin,name='blog-signin'),
    path('postsign/', views.postsign,name='blog-postsign'),
    path('register/', views.register,name='blog-register'),
    path('postregister/', views.postregister,name='blog-postregister'),
    # path('logout/', views.logout,name='blog-logout'),
    path('users/',views.UserListAV.as_view(),name="register_user"),
    path('<str:pk>',views.UserDetailsAV.as_view(),name="user_details"),
]