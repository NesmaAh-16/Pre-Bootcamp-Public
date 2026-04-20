# Bank Account Logic: Interest & Method Chaining

This module defines a `BankAccount` class that simulates financial transactions, including interest accrual and overdraft protection. It focuses on the **Fluent Interface** design pattern (Method Chaining).

## 🚀 Features

- **Method Chaining:** All state-changing methods return `self`, allowing for sequential operations in a single line of code.
- **Dynamic Initialization:** Supports custom interest rates and starting balances with sensible defaults.
- **Overdraft Protection:** Includes logic to detect insufficient funds and apply a penalty fee rather than allowing a negative transaction.
- **Interest Calculation:** A `yield_interest` method that applies a percentage-based increase to the current balance, provided the balance is positive.

## 🛠️ Technical Concepts
- **Fluent Interface:** Returning the instance (`self`) to allow concatenated method calls.
- **Conditional Logic:** Validating transaction viability before modifying the state.
- **Default Arguments:** Using `balance=0` in the constructor to allow flexible object instantiation.

## 📋 Execution Examples
- **Account A:** Demonstrates multiple deposits and a withdrawal followed by interest calculation.
- **Account B:** Demonstrates the overdraft logic where a withdrawal exceeds the balance, triggering a penalty fee before interest is applied.

## 💻 Usage
```python
# Create an account with 2% interest
account = BankAccount(0.02, 100)

# Chain multiple operations
account.deposit(50).withdraw(20).yield_interest().display_account_info()