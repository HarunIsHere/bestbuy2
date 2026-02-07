from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Return total price after applying promotion."""
        raise NotImplementedError


class PercentDiscount(Promotion):
    """Percentage discount promotion."""

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    """Second item at half price (per pair)."""

    def apply_promotion(self, product, quantity):
        pairs = quantity // 2
        remainder = quantity % 2
        return pairs * (product.price * 1.5) + remainder * product.price


class ThirdOneFree(Promotion):
    """Buy 2 get 1 free (every 3rd free)."""

    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        payable = quantity - free_items
        return payable * product.price
