from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.shop.serializers import (
    AddProductToCartSerializer,
)
class CreateProductAPI(APIView):
    authentication_classes = []
    permission_classes = []
    required_permissions = {'post':'can_add_product'}
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer['name']
            city = serializer['city']
            category = serializer['category']
            price = serializer['price']
            product = ProductService.create_product(name=name, city=city, category=category, price=price)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)