from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name):
        """Create a promotion with a name."""
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Return total price after applying promotion."""
        raise NotImplementedError


class PercentDiscount(Promotion):
    """Percentage discount promotion."""

    def __init__(self, name, percent):
        """Create a percent discount promotion."""
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        """Return total price after applying a percentage discount."""
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    """Second item at half price (per pair)."""

    def apply_promotion(self, product, quantity):
        """Return total price where every second item costs half."""
        pairs = quantity // 2
        remainder = quantity % 2
        return pairs * (product.price * 1.5) + remainder * product.price


class ThirdOneFree(Promotion):
    """Buy 2 get 1 free."""

    def apply_promotion(self, product, quantity):
        """Return total price where every third item is free."""
        free_items = quantity // 3
        payable = quantity - free_items
        return payable * product.price
