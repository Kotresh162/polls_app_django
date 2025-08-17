from django.shortcuts import get_object_or_404
from api.serializers import ProductSerializer,OrderSerilizer,ProductInfoSerializes
from api.models import Product,Order,OrderItem
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Max
from rest_framework import generics

# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products,many=True)
#     return Response(serializer.data)

class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class  = ProductSerializer

# @api_view(['GET'])
# def product_detail(request,id):
#     product = get_object_or_404(Product,pk=id)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)
class ProductDetailApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class  = ProductSerializer
    lookup_url_kwarg = 'id'


# @api_view(['GET'])
# def order_list(request):
#     orders = Order.objects.all()
#     serializer = OrderSerilizer(orders,many=True)
#     return Response(serializer.data)
class OrderListApi(generics.ListCreateAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class  = OrderSerilizer

class UserOrderListApi(generics.ListCreateAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class  = OrderSerilizer
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user = self.request.user)

@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializes({
        'products' : products,
        'count' : len(products),
        'max_price' : products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(serializer.data)
