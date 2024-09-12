from rest_framework import serializers

from apps.shop.models import (
    CustomUser, Cart, Product, 
    Category, ViewPoint, Address
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username')


class AddRemoveProductCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()


class UpdateProductInCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'is_paid', 'is_active', 'total_count', 'total_price')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'city', 'category', 'price')


class ListProductSerializer(serializers.ModelSerializer):
    price_lte = serializers.IntegerField()
    price_gte = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ('id', 'name', 'city', 'category', 'price_lte', 'price_gte')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'user', 'city', 'main_avenue', 'street', 'other_desc')


class ViewpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewPoint
        fields = ('id', 'product_id', 'score', 'content_text')


