import unittest
from decimal import Decimal
from checkout import Item, calculate_quote


class CouponTests(unittest.TestCase):
    def test_save20_happy_path(self):
        quote = calculate_quote([Item("HEADPHONES", Decimal("100.00"), 1)], coupon="save20")
        self.assertEqual(quote.discount, Decimal("20.00"))
        self.assertEqual(quote.shipping, Decimal("0.00"))
        self.assertEqual(quote.total, Decimal("80.00"))

    def test_invalid_code_rejected(self):
        with self.assertRaises(ValueError):
            calculate_quote([Item("A", Decimal("100.00"), 1)], coupon="INVALID")

    def test_minimum_spend_enforced(self):
        with self.assertRaises(ValueError):
            calculate_quote([Item("A", Decimal("49.99"), 1)], coupon="SAVE20")

    def test_coupon_whitespace_ignored(self):
        quote = calculate_quote([Item("A", Decimal("100.00"), 1)], coupon=" SAVE20 ")
        self.assertEqual(quote.total, Decimal("80.00"))


if __name__ == "__main__":
    unittest.main()
