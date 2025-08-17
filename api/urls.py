from django.urls import path
from . import views

urlpatterns = [
    path("products/",views.ProductListCreateApi.as_view()),
    path("orders/",views.OrderListApi.as_view()),
    path("user-orders/",views.UserOrderListApi.as_view()),
    path("products/<int:id>/",views.ProductDetailApi.as_view()),
    path("products/info/",views.ProductInfoApiView.as_view()),
]
