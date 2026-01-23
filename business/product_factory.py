from abc import ABC, abstractmethod

# Abstract base class for a product
class Product(ABC):
    @abstractmethod
    def get_details(self):
        pass


# Concrete Product implementations
class DigitalProduct(Product):
    def get_details(self):
        return "This is a digital product."


class PhysicalProduct(Product):
    def get_details(self):
        return "This is a physical product."


# Factory class
class ProductFactory:
    @staticmethod
    def create_product(product_type):
        if product_type == "digital":
            return DigitalProduct()
        elif product_type == "physical":
            return PhysicalProduct()
        else:
            raise ValueError(f"Unknown product type: {product_type}")