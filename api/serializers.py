from rest_framework import serializers
from sqlalchemy import true
from .models import Product,Order,OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',  # Assuming this is spelled the same in your model
            'price',
            'stock'
        )
        
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than zero"
            )
        return value
    
class OrderItemSerlizer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'product',
            'qauntity'
        )

class OrderSerilizer(serializers.ModelSerializer):
    items = OrderItemSerlizer(many=True,read_only=True)
    
    class Meta:
        model = Order
        fields = (
            'ordered_id',
            'user',
            'created_time',
            'status',
            'items'
        )
        