from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('',views.list,name="list"),
    path('login',views.login_user,name="login"),
    path('signup',views.signup_user,name="signup"),
    path('logout',views.logout_user,name="logout")
]