from django.contrib import admin
from django.urls import path, include
from myapp import views
from .views import logout_user
                            
urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.login_user,name="login"),
    path('signup',views.signup_user,name="signup"),
    path('create/', views.create_list, name='create_list'),
    path('lists/', views.lists, name='lists'),
    path('items<int:pk>//',views.list_detail,name='items'),
    path('logout',views.logout_user,name="logout")
]