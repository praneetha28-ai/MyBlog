from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('addpost',views.addpost,name="addpost"),
    path('',views.Home,name="home"),
    path('detail/<int:item>',views.viewDetail,name = "viewpost")
]
