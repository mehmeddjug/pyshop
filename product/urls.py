from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='home_products'),
    path('product/add', views.create_product, name='create_product'),
    path('product/', views.get_products, name='get_products'),
    path('product/<int:product_id>', views.get_product_by_id, name='get_product_by_id'),
    path('product/update/<int:product_id>', views.update_product_by_id, name='update_product'),
    path('product/delete/<int:product_id>', views.delete_product_by_id, name='delete_product'),
]