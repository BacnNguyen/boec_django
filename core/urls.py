
from django.urls import path
from .views import HomeView
from product.views import ProductView
app_name='core'
urlpatterns = [
    path('',HomeView.as_view(),name="index"),
    path('product/',ProductView.as_view(),name='product_view')
]
