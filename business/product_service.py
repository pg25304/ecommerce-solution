#product service.py
#pg25304 UoEO service(Business Layer) - product Management
#ProductService, which contains the business logic for handling product-related operations like adding and retrieving products
from business.models import Product
class ProductService:
    def __init__(self, product_repo):
        self.product_repo = product_repo

    def add_product(self, product_id, name, price, stock):
        """Creates a new Product object and saves it to the repository."""
        product = Product(product_id, name, price, stock)
        self.product_repo.save(product)
        return product

    def get_product(self, product_id):
        """Retrieves a product by its product_id."""
        return self.product_repo.find(product_id)

    def list_products(self):
        """Returns a list of all products in the repository."""
        return self.product_repo.list_all()