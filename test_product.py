"""Unit tests for the Product class using pytest."""

import pytest
from products import Product


def test_creating_prod():
    """Test that creating a normal product works."""
    p = Product("MacBook Air M2", price=1450, quantity=100)
    assert p.name == "MacBook Air M2"
    assert p.price == 1450
    assert p.get_quantity() == 100
    assert p.is_active() is True


def test_creating_prod_invalid_details():
    """Test that creating a product with invalid details raises exception."""
    with pytest.raises(Exception):
        Product("", price=1450, quantity=100)

    with pytest.raises(Exception):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_prod_becomes_inactive():
    """Test that a product becomes inactive when its quantity reaches 0."""
    p = Product("MacBook Air M2", price=1450, quantity=1)
    p.buy(1)
    assert p.get_quantity() == 0
    assert p.is_active() is False


def test_buy_modifies_quantity():
    """Test that buying a product returns correct total, reduces quantity."""
    p = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    total = p.buy(3)
    assert total == 750
    assert p.get_quantity() == 497


def test_buy_too_much():
    """Test that buying more than available quantity raises an exception."""
    p = Product("Google Pixel 7", price=500, quantity=2)
    with pytest.raises(Exception):
        p.buy(3)
