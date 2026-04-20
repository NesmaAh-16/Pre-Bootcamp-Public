# User Banking Interface: Method Chaining

This project implements a `User` class that simulates basic banking operations. It utilizes **Method Chaining** to allow multiple transactions to be executed in a single, readable line of code.

## 🚀 Features

- **Fluent API Design:** All state-modifying methods return `self`, allowing for chained calls like `.make_deposit(100).make_withdrawal(50).display_user_balance()`.
- **Account Management:** Supports deposits, withdrawals, and balance tracking for individual user instances.
- **Peer-to-Peer Transfers:** A built-in `transfer_money` method allows instances to interact, moving funds from the caller to a target user.
- **Formatted Reporting:** Clear console output for user balances using f-strings.

## 🛠️ Technical Concepts
- **Encapsulation:** Grouping user data (name/email) with their financial behaviors.
- **Method Chaining:** Returning the object instance to enable sequential method execution.
- **Inter-Object Communication:** Demonstrating how one object can modify the state of another object passed as an argument.

## 📋 Usage Example

```python
# Create a user and perform multiple actions in one line
guido = User("Guido van Rossum", "guido@python.com")
guido.make_deposit(100).make_deposit(200).make_withdrawal(50).display_user_balance()