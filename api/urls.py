from django.urls import path
from . import views

urlpatterns = [
    path("products/",views.ProductListApi.as_view()),
    path("orders/",views.OrderListApi.as_view()),
    path("products/<int:id>/",views.ProductDetailApi.as_view()),
    path("products/info/",views.product_info),
]
