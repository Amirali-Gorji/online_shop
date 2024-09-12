from apps.shop.models import ( 
    Cart, CartItem, Product,
    ViewPoint, Address, Category
)


class ProductService:
    @staticmethod
    def create_product(*, name, city, category, price):
        product = Product.objects.create(name=name, price=price)
        if product:
            product.category.add(*category)
            product.city.add(*city)
        return product


    @staticmethod
    def delete_product(*, product=None):
        product.category.clear()
        product.city.clear()
        product.delete()


    @staticmethod
    def update_product(*, product=None, name=None, city=None, category=None, price=None):
        update_product = False
        if name:
            product.name = name
            update_product = True
        if city:
            product.city.clear()
            product.city.add(*city)
            update_product = True
        if category:
            product.category.clear()
            product.category.add(*category)
            update_product = True
        if price:
            product.price = price
            update_product = True
        if update_product:
            product.save()
        return product


class CartItemService:
    @staticmethod
    def create_cart_item(* , cart=None, product=None, items_count=0, items_price=0):
        cart_item = CartItem.objects.create(cart=cart, product=product,
                                items_count=items_count, items_price=items_price)
        return cart_item


class CartService:
    @staticmethod
    def add_product_to_cart(*, user_id=None, product_id=None):
        cart = Cart.objects.get(user_id=user_id)
        try: 
            product = Product.objects.get(product_id=product_id)
        except Product.DoesNotExist:
            return None, "product_id doesn't exist"
        
        cart_item = CartItem.objects.filter(cart=cart, product=product_id)
        if not cart_item:
            cart_item = CartItemService.create_cart_item(cart=cart, product=product)
            
        
        if cart.total_count <= 9:
            cart_item.items_count += 1
            cart_item.items_price += product.price
            cart.total_count += 1
            cart.total_price += product.price
            cart_item.save()
            cart.save()
        else:
            return None, "Cart is full"
        
        return cart, "OK"
 
    @staticmethod
    def update_product_in_cart(*, user_id=None, product_id=None, quantity=0):
        # Check if this product exist in cart
        cart = Cart.objects.get(user_id=user_id)
        cart_item = CartItem.objects.filter(cart=cart, product=product_id)
        if not cart_item:
            return None, "CartItem with this product_id doesn't exist"

        product = Product.objects.get(product_id=product_id)
        cart_item = cart_item.first()

        if cart.total_count - quantity >= 1 and cart_item.items_count - quantity >= 1:
            cart_item.items_count -= quantity
            cart_item.items_price -= quantity * product.price
            cart.total_count -= quantity
            cart.total_price -= quantity * product.price
            cart_item.save()
            cart.save()
        else:
            return None, "Can't subtract this number of items"
        return cart, "OK"
    
    @staticmethod
    def remove_product_from_cart(*, user_id=None, product_id=None):
        # Check if this product exist in cart
        cart = Cart.objects.get(user_id=user_id)
        cart_item = CartItem.objects.filter(cart=cart, product=product_id)
        if not cart_item:
            return None, "CartItem with this product_id doesn't exist"

        cart_item = cart_item.first()

        cart_item.delete()

        return cart, "OK"


class CategoryService:
    @staticmethod
    def create_category(*, name):
        category = Category.objects.create(name=name)
        return category


class AddressService:
    @staticmethod
    def create_address(*, user=None, city=None, main_avenue=None, street=None, other_desc=None):
        insert_dict = {
            'user': user,
            'city': city,
            'main_avenue': main_avenue,
            'street': street
        }
        if other_desc:
            insert_dict['other_desc'] = other_desc
        address = Address(**insert_dict)
        address.save()
        return address
    

class ViewPointService:
    @staticmethod
    def add_viewpoint(*, user_id, product_id, score, content_text=None):
        viewpoint = ViewPoint.objects.create(user=user_id, product=product_id,
                                              score=score, content_text=content_text)
        return viewpoint

    @staticmethod
    def delete_viewpoint(*, viewpoint=None):
        viewpoint.delete()

