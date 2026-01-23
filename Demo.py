from data.user_repository import UserRepository
from data.product_repository import ProductRepository
from data.order_repository import OrderRepository

from business.user_services import UserService
from business.product_service import ProductService
from business.order_service import OrderService

from presentation.user_controller import UserController
from business.strategies import StrongPasswordValidationStrategy

#setup repositories
user_pro = UserRepository()
product_repo = ProductRepository()
order_repo = OrderRepository()
# Setup repositories and services
user_strategy = StrongPasswordValidationStrategy()  # Use strong password rules
user_service = UserService(user_pro, user_strategy)
#setup services
#user_service = UserService(user_pro)
product_service = ProductService(product_repo)
order_service = OrderService(order_repo, product_repo)

#setup controllers
user_controller = UserController(user_service)

