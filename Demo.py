#demo of an e-commerce application using layered architecture
from data.user_repository import UserRepository
from data.product_repository import ProductRepository
from data.order_repository import OrderRepository

from business.user_services import UserService
from business.product_service import ProductService
from business.order_service import OrderService

from presentation.user_controller import UserController
from business.strategies import StrongPasswordValidationStrategy

# Setup repositories
user_repo = UserRepository()
product_repo = ProductRepository()
order_repo = OrderRepository()

# Setup services
user_strategy = StrongPasswordValidationStrategy()  # Use strong password rules for users
user_service = UserService(user_repo, user_strategy)
product_service = ProductService(product_repo)
order_service = OrderService(order_repo, product_repo)

# Setup controllers
user_controller = UserController(user_service)

# Demonstration of the Application
if __name__ == "__main__":
    print("Welcome to the E-commerce App Demo!")
    print("===================================")

    # User Registration
    print("\nStep 1: Register a User")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    try:
        user_controller.register_user(username, password)
        print(f"User '{username}' registered successfully!")
    except ValueError as e:
        print(f"Failed to register user: {e}")

    # Add a Product
    print("\nStep 2: Add Products to the Store")
    while True:
        product_name = input("Enter product name (or type 'done' to finish): ").strip()
        if product_name.lower() == 'done':
            break
        price = float(input("Enter product price: "))
        product_service.add_product(product_name, price)
        print(f"Product '{product_name}' added with price {price}")

    # Display All Products
    print("\nStep 3: Displaying All Products")
    products = product_service.get_all_products()
    for product in products:
        print(f"- {product['name']}: ${product['price']}")

    # Create an Order
    print("\nStep 4: Create an Order")
    selected_products = []
    while True:
        product_name = input("Enter the product name to add to the order (or type 'done' to finish): ").strip()
        if product_name.lower() == 'done':
            break
        selected_products.append(product_name)
    try:
        order = order_service.create_order(username, selected_products)
        print(f"Order created successfully! Order ID: {order['id']}")
    except ValueError as e:
        print(f"Failed to create order: {e}")

    # Display User Orders
    print("\nStep 5: Displaying Orders for the User")
    user_orders = order_service.get_orders_by_user(username)
    for order in user_orders:
        print(f"Order ID: {order['id']} - Products: {', '.join(order['products'])} - Total: ${order['total_price']}")

    print("\nDemo Complete. Thank you for using the E-commerce App!")