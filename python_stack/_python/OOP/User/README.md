# Banking System Emulation (OOP)

A Python-based simulation of a banking system using Object-Oriented Programming. This project demonstrates the core pillars of OOP, specifically **Encapsulation** and **Method Interaction**.

## 🚀 Features

- **Class-Based Architecture:** Uses a `User` class to bundle data (name, email, balance) and behavior (deposit, withdrawal).
- **Transaction Management:** 
  - `make_deposit`: Increases the user's account balance.
  - `make_withdrawal`: Decreases the user's account balance.
  - `transfer_money`: A sophisticated method that allows interaction between two separate class instances (objects).
- **State Tracking:** Keeps a persistent record of the user's financial state across multiple operations.

## 🛠️ Technical Concepts
- **The `__init__` Method:** Initializing unique attributes for each object instance.
- **Instance Methods:** Using `self` to access and modify the specific data of an object.
- **Object Interaction:** Passing one object into the method of another object (Dependency Injection).

## 📋 Logic Flow
1. **Instantiation:** Create unique user objects with defined emails and names.
2. **Operations:** Perform multiple deposits and withdrawals to simulate real-world usage.
3. **Cross-User Transfer:** Deduct funds from one instance and programmatically add them to another instance.
4. **Verification:** Display formatted output to verify the integrity of the math.

## 💻 How to Run
```bash on correct path
python main.py