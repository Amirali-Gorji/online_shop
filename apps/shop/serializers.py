from rest_framework import serializers

from apps.shop.models import (
    CustomUser, 
    CartItem, 
    Product, 
    Category, 
    ViewPoint, 
    Address
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')


class AddProductToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('cart', 'product', 'items_count', 'items_price')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'city', 'category', 'price')


class ListProductSerializer(serializers.ModelSerializer):
    price_lte = serializers.IntegerField()
    price_gte = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ('name', 'city', 'category', 'price_lte', 'price_gte')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('user', 'city', 'main_avenue', 'street', 'other_desc')


class ViewpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewPoint
        fields = ('product_id', 'score', 'content_text')


