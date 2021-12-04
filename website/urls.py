from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('register_product/', views.RegisterProduct.as_view(), name='register_product')
]