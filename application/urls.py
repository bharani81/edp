from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.landingpage,name="home"),
    path('login',views.login_request),
    path('register',views.login_register),
    path('logout',views.logout_request)
]
