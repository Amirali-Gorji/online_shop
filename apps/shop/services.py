from apps.shop.models import ( 
    Cart,
    CartItem,
    Product,
    ViewPoint, 
    Address,
    Category
)

class ViewPointService:
    @staticmethod
    def add_viewpoint(*, user_id, product_id, score, content_text=None):
        viewpoint = ViewPoint.objects.create(user=user_id, product=product_id,
                                              score=score, content_text=content_text)
        return viewpoint

    @staticmethod
    def delete_viewpoint(*, viewpoint=None):
        viewpoint.delete()
