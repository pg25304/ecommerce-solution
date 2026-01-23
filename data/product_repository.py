#product repository.py
#pg25304 UoEO - Data Access Layer - product catalog - product repository
#A repository class for managing product-related operations.
from data.base_repository import BaseRepository

class ProductRepository(BaseRepository):
    #The constructor method (__init__) is called when a new ProductRepository object is created.
    #It initializes the object, specifically the in-memory storage for products.
    def __init__(self):
        #In-memory storage for products
        self.products = {}
    #store a Product object in the repository.
    #It takes the product to be saved as an argument.
    def save(self, product):
        #Uses the product’s product_id as the key and the product object itself as the value.
        self.products[product.product_id] = product

    def find(self, product_id):
        return self.products.get(product_id)

    def list_all(self):
        return  list(self.products.values())


