"""Small dependency-free shopping cart pricing module."""

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from typing import Iterable

CENT = Decimal("0.01")
FREE_SHIPPING_THRESHOLD = Decimal("75.00")
FLAT_SHIPPING = Decimal("7.95")


@dataclass(frozen=True)
class Item:
    sku: str
    unit_price: Decimal
    quantity: int


@dataclass(frozen=True)
class Quote:
    subtotal: Decimal
    discount: Decimal
    shipping: Decimal
    total: Decimal


def money(amount: Decimal) -> Decimal:
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)


def cart_subtotal(items: Iterable[Item]) -> Decimal:
    """Validate line items and return their subtotal."""
    amount = Decimal("0.00")
    for item in items:
        if not item.sku.strip():
            raise ValueError("Item SKU must not be blank")
        if isinstance(item.quantity, bool) or not isinstance(item.quantity, int) or item.quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        if not item.unit_price.is_finite() or item.unit_price < 0:
            raise ValueError("Unit price must be a finite, nonnegative Decimal")
        amount += item.unit_price * item.quantity
    return money(amount)


def shipping_fee(pre_discount_subtotal: Decimal) -> Decimal:
    """Shipping is always based on merchandise BEFORE discounts."""
    return Decimal("0.00") if pre_discount_subtotal >= FREE_SHIPPING_THRESHOLD else FLAT_SHIPPING


def calculate_quote(items: Iterable[Item]) -> Quote:
    merchandise = cart_subtotal(items)
    shipping = shipping_fee(merchandise)
    return Quote(
        subtotal=merchandise,
        discount=Decimal("0.00"),
        shipping=shipping,
        total=money(merchandise + shipping),
    )
