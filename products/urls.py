from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('save/<int:product_id>/', views.save_product, name='save_product'),
    path('saved_products/', views.saved_products, name='saved_products'),
    path('saved_products/<int:saved_product_id>/delete/', views.delete_saved_product, name='delete_saved_product'),
]
