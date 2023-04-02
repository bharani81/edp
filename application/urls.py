from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.landingpage,name="home"),
    path('register',views.login_register),
    path('logout',views.logout_request),
    path('post_question',views.post_my_question),
    path('article',views.article,name="article"),
    path('accounts/', include('allauth.urls')),
    path('profile',views.my_profile),
    path('saveprofile',views.my_profile),
]
