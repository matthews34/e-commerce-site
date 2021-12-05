from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('product/register/', views.register_product, name='register_product'),
    path('product/list/', views.list_products, name='list_products'),
    path('product/<int:id>/', views.detail_product, name='datail_product'),
    path('product/<int:id>/update/', views.update_product, name='update_product'),
    path('product/<int:id>/delete/', views.delete_product, name='delete_product'),
    path('catalog/', views.catalog, name='catalog'),
    path('product/<int:product_id>/buy/', views.buy_product, name='buy_product')
]