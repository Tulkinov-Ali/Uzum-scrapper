from django.urls import path
from .views import index, process_product_view

urlpatterns = [
    path('', index, name='index'),
    path('process_product/', process_product_view, name='process_product'),
]