"""Each layer depends only on the one below it.
/presentation
/business
/data
"""
from business.product_factory import ProductFactory


if __name__ == "__main__":
    product_type = input("Enter product type (digital/physical): ").strip().lower()
    try:
        product = ProductFactory.create_product(product_type)
        print(product.get_details())
    except ValueError as e:
        print(e)