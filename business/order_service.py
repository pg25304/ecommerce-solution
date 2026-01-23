#order service - business layer
# A service class for handling order-related business logic.
# business/order_service.py
from business.models import Order
class OrderService:
    def __init__(self, order_repo, product_repo):
        self.order_repo = order_repo
        self.product_repo = product_repo

    def create_order(self, order_id, user, cart_items):
        items = []
        for product_id, qty in cart_items:
            product = self.product_repo.find(product_id)
            if product and product.stock >= qty:
                product.stock -= qty
                items.append((product, qty))
            else:
                raise Exception(f"Insufficient stock for product: {product.name if product else 'unknown'}")

        order = Order(order_id, user, items)
        self.order_repo.save(order)
        return order



