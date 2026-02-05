class Store:
    """Represents a store that holds and sells products."""

    def __init__(self, product_list):
        """Create a store with an initial list of products."""
        self.products = product_list

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self):
        """Return total quantity of all items in the store."""
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self):
        """Return a list of active products."""
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list):
        """Buy products from a list of (Product, quantity) and return total."""
        total_price = 0.0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception("Product not in store")
            total_price += product.buy(quantity)
        return total_price
