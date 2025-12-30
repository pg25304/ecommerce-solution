from data.user_repository import UserRepository
from data.product_repository import ProductRepository
from data.order_repository import OrderRepository

from business.user_services import UserService
from business.product_service import ProductService
from business.order_service import OrderService

from presentation.user_controller import UserController

#setup repositories
user_pro = UserRepository()
product_repo = ProductRepository()
order_repo = OrderRepository()

#setup services
user_service = UserService(user_pro)
product_service = ProductService(product_repo)
order_service = OrderService(order_repo, product_repo)

#setup controllers
user_controller = UserController(user_service)

#register a new user
new_user = user_controller.register_user(1, "jack@example.com", "securepassword")

#Add products
product_service.add_product(101, "Laptop", 999.99, 10)
product_service.add_product(102, "Smartphone", 499.99, 20)

#create an order
order = order_service.create_order(
    order_id=5001,
    user=new_user,
    cart_items=[(101, 1), (102, 2)]
)

print("Order created for:", order.user.email)
for product, qty in order.items:
    print(f"- {product.name} x{qty}")
