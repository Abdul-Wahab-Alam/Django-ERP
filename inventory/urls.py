from django.urls import path
from . import views

urlpatterns = [
    path('',views.inventory_index,name='inventory_home'),
    path('create/',views.create_product, name='create_product')
]