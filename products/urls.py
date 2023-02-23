from django.urls import path
from . import views


urlpatterns = [
     path('', views.all_products, name='products'),
     path('<int:product_id>/', views.product_detail, name='product_detail'),
     path('add_product/', views.add_product, name='add_product'),
     path('edit_product/<int:product_id>/',
          views.edit_product, name='edit_product'),
     path('delete_product/<int:product_id>/',
          views.delete_product, name='delete_product'),
     path('submit-review/', views.submit_review, name='submit_review'),
]
