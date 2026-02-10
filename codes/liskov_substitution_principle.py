"""Liskov Substitution Principle (LSP) demonstration using payment processors.

Subtypes must be substitutable for their base types without altering the
correctness of the program. CryptoPayment intentionally violates LSP by
strengthening the precondition (minimum 100$) beyond the base class contract.
"""

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """Abstract base class defining the contract for all payment processors."""

    @abstractmethod
    def pay(self, amount: float) -> None:
        """
        Contract:
        - amount must be > 0
        - raises ValueError if invalid
        - processes payment successfully otherwise
        """
        pass


class CreditCardPayment(PaymentProcessor):
    """Payment processor that handles credit card transactions."""

    def pay(self, amount: float) -> None:
        try:
            if amount <= 0:
                raise ValueError("Amount must be greater than zero")
            print(f"Paid {amount}$ using Credit Card")
        except ValueError:
            print("Amount must be greater than Zero")


class PayPalPayment(PaymentProcessor):
    """Payment processor that handles PayPal transactions."""

    def pay(self, amount: float) -> None:
        try:
            if amount <= 0:
                raise ValueError("Amount must be greater than zero")
            print(f"paid {amount}$ using paypal")
        except ValueError:
            print("Amount must be greater than zero")


class CashPayment(PaymentProcessor):
    """Payment processor that handles cash transactions."""

    def pay(self, amount: float) -> None:
        try:
            if amount <= 0:
                raise ValueError("Amount must be greater than zero")
            print(f"paid {amount}$ in cash")
        except ValueError:
            print("Amount must be greater than zero")


class CryptoPayment(PaymentProcessor):
    """Payment processor that handles cryptocurrency transactions.

    Violates LSP by strengthening the precondition: requires a minimum
    payment of 100$, which is stricter than the base class contract.
    """

    def pay(self, amount: float) -> None:
        try:
            if amount < 100:
                raise ValueError("Minimum crypto payment is 100$")
            print(f"Paid {amount}$ using Crypto")
        except ValueError:
            print(
                "Minimum crypto payment is 100$ (this method break liskov principle) "
            )


def process_payment(processor: PaymentProcessor, amount: float):
    """
    This function TRUSTS the base class contract.
    Any subclass must work here without breaking anything.
    """
    processor.pay(amount)


if __name__ == "__main__":
    payments = [CreditCardPayment(), PayPalPayment(), CashPayment(), CryptoPayment()]

    for payment in payments:
        process_payment(payment, 90)
