from django.contrib import admin
from django.urls import path, include
from myapp import views
from .views import logout_user
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name="home"),
    path('login',views.login_user,name="login"),
    path('signup',views.signup_user,name="signup"),
    path('create/', views.create_list, name='create_list'),
    path('lists/', views.lists, name='lists'),
    path("list/<int:list_id>/", views.list_detail, name="list_detail"),
    path('logout',views.logout_user,name="logout"),
    path('list/delete/<int:list_id>/', views.delete_list, name='delete_list'),
    path('item/delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('profile/',views.view_profile,name="profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   