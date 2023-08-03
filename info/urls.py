from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('faqs', views.view_faqs, name='faqs'),
    path('about', views.view_about, name='about'),
]
