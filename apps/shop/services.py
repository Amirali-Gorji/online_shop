from apps.shop.models import ( 
    Cart,
    CartItem,
    Product,
    ViewPoint, 
    Address,
    Category
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
class ViewPointService:
    @staticmethod
    def add_viewpoint(*, user_id, product_id, score, content_text=None):
        viewpoint = ViewPoint.objects.create(user=user_id, product=product_id,
                                              score=score, content_text=content_text)
        return viewpoint

    @staticmethod
    def delete_viewpoint(*, viewpoint=None):
        viewpoint.delete()
