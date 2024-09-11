from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.shop.services import ProductService, CategoryService, ViewPointService, AddressService
from apps.shop.selectors import (
    ProductSelector, 
    CategorySelector, 
    ViewPointSelector, 
    AddressSelector
)
from apps.shop.serializers import (
    AddProductToCartSerializer,
    ViewpointSerializer,
    CartItemSerializer,
    ProductSerializer,
    ListProductSerializer,
    CategorySerializer,
    AddressSerializer
)
from apps.shop.models import Product
from apps.utils.paginations import CustomPagination


class ListProductAPI(APIView, CustomPagination):
    # TODO: add city and name filter
    def get(self, request):
        serializer = ListProductSerializer(data=request.query_params)
        if serializer.is_valid(): 
            name = serializer.validated_data.get('name')
            city = serializer.validated_data.get('city')
            category = serializer.validated_data.get('category')
            price_lte = serializer.validated_data.get('price_lte')
            price_gte = serializer.validated_data.get('price_gte')
            products = ProductSelector.get_products(name=name, city=city, category=category,
                                                    price_gte=price_gte, price_lte=price_lte)
            page = self.paginate_queryset(products, request)
            serializer = ProductSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        
class CreateProductAPI(APIView):
    authentication_classes = []
    permission_classes = []
    required_permissions = {'post':'can_add_product'}
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            city = serializer.validated_data.get('city')
            category = serializer.validated_data.get('category')
            price = serializer.validated_data.get('price')
            product = ProductService.create_product(name=name, city=city, category=category, price=price)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProductAPI(APIView):
    authentication_classes = []
    permission_classes = []
    required_permissions = {'delete':'can_delete_product'}

    def delete(self, product_id=None):
        product = ProductSelector.get_product(product_id==product_id)
        if not product:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        ProductService.delete_product(product=product)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateProductAPI(APIView):
    authentication_classes = []
    permission_classes = []
    required_permissions = {'post':'can_update_product'}

    def put(self, request, product_id=None):
        product = ProductSelector.get_product(product_id=product_id)
        if not product:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            city = serializer.validated_data.get('city')
            category = serializer.validated_data.get('category')
            price = serializer.validated_data.get('price')
            product = ProductService.update_product(product=product, name=name, city=city, category=category, price=price)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class CreateCategoryAPI(APIView):
    authentication_classes = []
    permission_classes = []
    required_permissions = {'post':'can_add_category'}
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            category = CategoryService.create_category(name=name)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ListCategoryAPI(APIView, CustomPagination):
    authentication_classes = []
    permission_classes = []
    required_permissions = {'get':'can_get_category'}
    
    def get(self, request):
        categories = CategorySelector.get_categories()
        page = self.paginate_queryset(categories, request)
        serializer = CategorySerializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class ListAddressAPI(APIView, CustomPagination):
    authentication_classes = []
    permission_classes = []
    required_permissions = {'get':'can_get_address'}
    
    def get(self, request):
        addresses = AddressSelector.get_categories()
        page = self.paginate_queryset(addresses, request)
        serializer = AddressSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class CreateAddressAPI(APIView):
    authentication_classes = []
    permission_classes = []
    required_permissions = {'post':'can_add_address'}
    
    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            address = AddressService.create_category(name=name)
            serializer = AddressSerializer(address)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CreateViewPointAPI(APIView):
    authentication_classes = []
    permission_classes = []
    required_permissions = {'post':'can_add_viewpoint'}

    def post(self, request, product_id):
        serializer = ViewpointSerializer(data=request.data)
        if serializer.is_valid():
            score = serializer.validated_data.get('score')
            content_text = serializer.validated_data.get('content_text')
            viewpoint = ViewPointService.add_viewpoint(request.user.id, product_id=product_id,
                        score=score, content_text=content_text)
            serializer = ViewpointSerializer(viewpoint)
            return Response(serializer.data)
    

class DeleteViewPointAPI(APIView):
    authentication_classes = []
    permission_classes = []
    required_permissions = {'delete':'can_delete_viewpoint'}

    def delete(self, viewpoint_id=None):
        viewpoint = ViewPointSelector.get_viewpoint(viewpoint_id=viewpoint_id)
        if not viewpoint:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        ViewPointService.delete_viewpoint(viewpoint=viewpoint)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListViewPointAPI(APIView, CustomPagination):
    def get(self, request, product_id=None):
        viewpoints = ViewPointSelector.get_product_viewpoints(product_id=product_id)
        page = self.paginate_queryset(viewpoints, request)
        serializer = ViewpointSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
