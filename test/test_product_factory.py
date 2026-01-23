# Unit tests for the ProductFactory class in business/product_factory.py
import unittest
from business.product_factory import ProductFactory, DigitalProduct, PhysicalProduct

class TestProductFactory(unittest.TestCase):
    def test_digital_product_creation(self):
        product = ProductFactory.create_product("digital")
        self.assertIsInstance(product, DigitalProduct)
        self.assertEqual(product.get_details(), "This is a digital product.")

    def test_physical_product_creation(self):
        product = ProductFactory.create_product("physical")
        self.assertIsInstance(product, PhysicalProduct)
        self.assertEqual(product.get_details(), "This is a physical product.")

    def test_invalid_product_creation(self):
        with self.assertRaises(ValueError):
            ProductFactory.create_product("unknown")

if __name__ == "__main__":
    unittest.main()