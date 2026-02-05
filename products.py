class Product:
    """Represents a product available in the store."""

    def __init__(self, name, price, quantity):
        """Create a new Product."""
        if not isinstance(name, str) or name.strip() == "":
            raise Exception("Product name must be a non-empty string")
        if price < 0:
            raise Exception("Product price cannot be negative")
        if quantity < 0:
            raise Exception("Product quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if self.quantity == 0:
            self.active = False

    def get_quantity(self):
        """Return current quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set quantity; deactivate if it becomes 0."""
        if quantity < 0:
            raise Exception("Quantity cannot be negative")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self):
        """Return True if product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print a string representation of the product."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """Buy a quantity and return total price."""
        if quantity <= 0:
            raise Exception("Buy quantity must be greater than 0")
        if not self.is_active():
            raise Exception("Cannot buy an inactive product")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price
