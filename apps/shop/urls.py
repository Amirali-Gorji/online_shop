from django.urls import path

from apps.shop.views import (
    CreateViewPointAPI, DeleteViewPointAPI, ListViewPointAPI,
    CreateProductAPI, DeleteProductAPI, AddProductToCartAPI,
    UpdateCartProductAPI, CreateCategoryAPI, ListProductAPI, 
    ListCategoryAPI, UpdateProductAPI, ListAddressAPI,
    CreateAddressAPI, RemoveProductFromCart
)


urlpatterns = [
    path('products/', ListProductAPI.as_view(), name='list-products'),
    path('products/create/', CreateProductAPI.as_view(), name='create-product'),
    path('products/<int:product_id>/update/', UpdateProductAPI.as_view(), name='update-products'),
    path('products/<int:product_id>/delete/', DeleteProductAPI.as_view(), name='delete-product'),
    path('products/<int:product_id>/viewpoints/', ListViewPointAPI.as_view(), name='list-product-viewpoints'),
    path('products/<int:product_id>/viewpoints/create/', CreateViewPointAPI.as_view(), name='create-product-viewpoint'),
    path('products/<int:product_id>/viewpoints/<int:viewpoint_id>/delete/', DeleteViewPointAPI.as_view(), name='delete-viewpoint'),
    path('cart/add/', AddProductToCartAPI.as_view(), name='add-product-to-cart'),
    path('cart/update/', UpdateCartProductAPI.as_view(), name='update-product-in-cart'),
    path('cart/remove/', RemoveProductFromCart.as_view(), name='remove-product-from-cart'),
    # path('cart/payment/', .as_view(), name='pay-cart'),
    path('categories/', ListCategoryAPI.as_view(), name='list-categories'),
    path('categories/create/', CreateCategoryAPI.as_view(), name='create-categories'),
    path('address/', ListAddressAPI.as_view(), name='list-address'),
    path('address/create/', CreateAddressAPI.as_view(), name='create-address'),
]

