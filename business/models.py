#pg25304 UoEO - Domain Nodel (Business layer) - user Management

class User:
    def __init__(self, user_id, email, password_hash):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
#product catalog - Domain model
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
#order model -  Domainmodel
class Order:
    def __init__(self, order_id, user, items):
        self.order_id = order_id
        self.user = user
        self.items = items  # List of OrderItem objects