from rest_framework import serializers

from apps.shop.models import CustomUser, CartItem, Product, Category, ViewPoint, Address



class ProductSelector:
    @staticmethod
    def get_product(*, product_id=None):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return None
        return product

    @staticmethod
    def get_products(*, name=None, city=None, category=None,
                        price_gte=None, price_lte=None):
        search_params = {}
        if name:
            search_params['name'] = name
        if city:
            search_params['city'] = city
        if category:
            search_params['category__in'] = category
        if price_gte:
            search_params['price_gte'] = price_gte
        if price_lte:
            search_params['price_lte'] = price_lte
        
        products = Product.objects.filter(**search_params)
        return products


class CategorySelector:
    @staticmethod
    def get_categories():
        try:
            categories = Category.objects.filter()
        except Category.DoesNotExist:
            return None
        return categories


class AddressSelector:
    @staticmethod
    def get_categories():
        try:
            address = Address.objects.filter()
        except Address.DoesNotExist:
            return None
        return address


class ViewPointSelector:
    @staticmethod
    def get_viewpoint(*, viewpoint_id=None):
        try:
            viewpoint = ViewPoint.objects.get(id=viewpoint_id)
        except ViewPoint.DoesNotExist:
            return None
        return viewpoint
    
    @staticmethod
    def get_product_viewpoints(*, product_id=None):
        search_params = {}
        if product_id:
            search_params['product_id'] = product_id
        
        viewpoints = ViewPoint.objects.filter(**search_params)
        return viewpoints
    
