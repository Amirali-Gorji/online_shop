from rest_framework import serializers

from apps.shop.models import CustomUser, CartItem, Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'city', 'category', 'price')
