from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('task/', views.task, name='task'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('deletetask/<str:slug>', views.deletetask, name='deletetask'),
    path('edittask/<str:slug>', views.edittask, name='edittask'),
]
