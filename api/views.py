from django.shortcuts import get_object_or_404
from api.serializers import ProductSerializer,OrderSerilizer
from api.models import Product,Order,OrderItem
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request,id):
    product = get_object_or_404(Product,pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerilizer(orders,many=True)
    return Response(serializer.data)
