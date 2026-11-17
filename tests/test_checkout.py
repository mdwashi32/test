import unittest
from decimal import Decimal
from checkout import Item, calculate_quote, cart_subtotal


class CheckoutTests(unittest.TestCase):
    def test_free_shipping_at_75(self):
        quote = calculate_quote([Item("SHIRT", Decimal("75.00"), 1)])
        self.assertEqual(quote.shipping, Decimal("0.00"))
        self.assertEqual(quote.total, Decimal("75.00"))

    def test_shipping_below_75(self):
        quote = calculate_quote([Item("SHIRT", Decimal("60.00"), 1)])
        self.assertEqual(quote.shipping, Decimal("7.95"))
        self.assertEqual(quote.total, Decimal("67.95"))

    def test_multiple_items(self):
        quote = calculate_quote([
            Item("A", Decimal("19.99"), 2),
            Item("B", Decimal("10.00"), 1),
        ])
        self.assertEqual(quote.subtotal, Decimal("49.98"))
        self.assertEqual(quote.total, Decimal("57.93"))

    def test_negative_quantities_rejected(self):
        with self.assertRaises(ValueError):
            cart_subtotal([Item("A", Decimal("20.00"), -1)])

    def test_non_finite_prices_rejected(self):
        with self.assertRaises(ValueError):
            cart_subtotal([Item("A", Decimal("NaN"), 1)])


if __name__ == "__main__":
    unittest.main()
