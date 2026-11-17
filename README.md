# CodeRabbit PR Review Demo: Checkout Pricing

A deliberately tiny, dependency-free Python checkout calculator for demonstrating how an AI code reviewer identifies business-logic regressions in a pull request.

## Product rules

- Subtotal = sum of unit price times quantity.
- Shipping costs **$7.95** if the **pre-discount** subtotal is below **$75**; otherwise shipping is free.
- The next feature adds coupon `SAVE20`, which gives **20% off merchandise**, capped at **$25**, when the **pre-discount** subtotal is at least **$50**.
- Invalid coupon codes and attempts to use the coupon below the minimum should raise `ValueError`.
- Only merchandise is discounted; shipping is never discounted.
- Monetary totals use `decimal.Decimal` and cents rounding.

## Run tests

Python 3.10+; no third-party packages required:

```bash
python3 -m unittest discover -s tests -v
```

## Why this is a good PR review exercise

The baseline tests cover ordinary shipping and cart validation. The feature branch adds coupons and happy-path tests, but has **two subtle business-logic regressions**. The goal is to have a reviewer discover the issues, validate them with focused regression tests, and fix them. A reviewer's suggestions are not guaranteed, so examine the diff yourself too.

See the separate `INTERVIEW_GUIDE.md` outside the repository for setup, a presentation script, and the post-review fix.
