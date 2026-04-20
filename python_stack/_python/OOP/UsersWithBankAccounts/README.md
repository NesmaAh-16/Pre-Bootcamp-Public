# Multi-Account Banking System (Advanced OOP)

This project demonstrates an advanced implementation of Object-Oriented Programming (OOP) in Python, focusing on **Association** and **Data Structuring**. A `User` can manage multiple named `BankAccount` instances using a dictionary-based system.

## 🚀 Features

- **Class Association:** The `User` class acts as a manager for `BankAccount` objects.
- **Multiple Account Support:** Accounts are stored in a dictionary, allowing users to differentiate between different account types (e.g., "test_account_A", "test_account_B").
- **Encapsulated Transactions:** logic for deposits and withdrawals is centralized within the `BankAccount` class.
- **Peer-to-Peer Transfers:** Enhanced `transfer_money` method that supports moving funds between specific accounts of different users.
- **Dynamic Reporting:** `display_user_balance` iterates through all accounts associated with a user to provide a full financial summary.

## 🛠️ Technical Concepts

- **Composition/Association:** Building complex classes by using instances of other classes as attributes.
- **Dictionary Mapping:** Using keys to retrieve specific object instances from a collection.
- **Cross-Object Method Invocations:** Methods that accept other object instances as arguments to facilitate interaction.

## 📋 Example Workflow
1. User A deposits into their "test_account_A".
2. User A transfers money from their "test_account_A" to User B's "test_account_B".
3. Both users display their balances to verify the multi-account state change.

## 💻 How to Run
```bash to the correct path
python main.py