

# SOLID Principles in Python

A collection of practical Python examples demonstrating each of the five SOLID principles of object-oriented design.

![SOLID Principles](assets/images/solid.png)


## What is SOLID?

SOLID is a set of five design principles introduced by Robert C. Martin that help developers write code that is easy to maintain, extend, and understand.

| Principle | Full Name | Summary |
|-----------|-----------|---------|
| **S** | Single Responsibility | A class should have only one reason to change |
| **O** | Open/Closed | Open for extension, closed for modification |
| **L** | Liskov Substitution | Subtypes must be substitutable for their base types |
| **I** | Interface Segregation | Prefer many small interfaces over one large interface |
| **D** | Dependency Inversion | Depend on abstractions, not concretions |

## Project Structure

```
SOLID Principles/
├── LiskovsSubstitutionPrinciple.py  
├── requirements.txt
├── README.md
└── venv/
```

## Principles & Examples

### L — Liskov Substitution Principle

**File:** `Liskov'sSubstitutionPrinciple.py`

Demonstrates that any subclass of `PaymentProcessor` (CreditCard, PayPal, Cash) can be used interchangeably without breaking the `process_payment` function. Every subclass honors the same contract defined by the base class.

```python
payments = [CreditCardPayment(), PayPalPayment(), CashPayment()]

for payment in payments:
    process_payment(payment, 100)  # works with any PaymentProcessor subtype
```

### S — Single Responsibility Principle
*Coming soon*

### O — Open/Closed Principle
*Coming soon*

### I — Interface Segregation Principle
*Coming soon*

### D — Dependency Inversion Principle
*Coming soon*

## Getting Started

### Prerequisites

- Python 3.x

### Setup

```bash
# Clone the repository
git clone <repository-url>
cd "SOLID Principles"

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

### Running an Example

```bash
python "Liskov'sSubstitutionPrinciple.py"
```

## License

This project is open source and available for educational purposes.
