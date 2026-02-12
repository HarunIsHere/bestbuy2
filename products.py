class Product:
    """A product available in the store."""

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
        self.promotion = None

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

    def get_promotion(self):
        """Return current promotion (or None)."""
        return self.promotion

    def set_promotion(self, promotion):
        """Set promotion (Promotion or None)."""
        self.promotion = promotion

    def __str__(self):
        """Return a string representation of the product."""
        promo_name = self.promotion.name if self.promotion else "None"
        return (
            f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, "
            f"Promotion: {promo_name}"
        )

    def show(self):
        """Print a string representation of the product."""
        print(str(self))

    def buy(self, quantity):
        """Buy a quantity and return total price."""
        if quantity <= 0:
            raise Exception("Buying quantity must be greater than 0")
        if not self.is_active():
            raise Exception("Cannot buy an inactive product")
        if quantity > self.quantity:
            raise Exception("There is not enough in stock")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    """A product that has no stock limit (e.g., Software)."""

    def __init__(self, name, price):
        """Create a non-stocked product with unlimited quantity."""
        super().__init__(name, price, quantity=0)
        self.activate()

    def set_quantity(self, quantity):
        """Quantity is always 0 for non-stocked products."""
        self.quantity = 0
        self.activate()

    def __str__(self):
        """Return a string representation of the non-stocked product."""
        promo_name = self.promotion.name if self.promotion else "None"
        return (
            f"{self.name}, Price: {self.price}, Quantity: Unlimited, "
            f"Promotion: {promo_name}"
        )

    def show(self):
        """Print a string representation including unlimited quantity."""
        print(str(self))

    def buy(self, quantity):
        """Buy without an effect on quantity."""
        if quantity <= 0:
            raise Exception("Buy quantity must be greater than 0")
        if not self.is_active():
            raise Exception("Cannot buy an inactive product")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity


class LimitedProduct(Product):
    """A product that can only be bought up to 'maximum' times per order."""

    def __init__(self, name, price, quantity, maximum):
        """Create a limited product with a per-order maximum."""
        super().__init__(name, price, quantity)
        if maximum < 1:
            raise Exception("Maximum must be at least 1")
        self.maximum = maximum

    def buy(self, quantity):
        """Buy a quantity up to the per-order maximum."""
        if quantity > self.maximum:
            raise Exception("Quantity exceeds maximum allowed per order")
        return super().buy(quantity)

    def __str__(self):
        """Return a string representation including the per-order maximum."""
        promo_name = self.promotion.name if self.promotion else "None"
        return (
            f"{self.name}, Price: {self.price}, "
            f"Limited to {self.maximum} per order!, Promotion: {promo_name}"
        )

    def show(self):
        """Print a string representation including the per-order maximum."""
        print(str(self))
