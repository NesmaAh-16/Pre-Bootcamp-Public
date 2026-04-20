# Python Function Mechanics & List Algorithms

This repository focuses on understanding the inner workings of Python functions. It is divided into two sections: a deep dive into function execution flows (returns, scopes, and side effects) and foundational list manipulation algorithms.

## 🚀 Features

### Section 1: Function Prediction & Scope
- **Return vs. Print:** Visualizing the difference between returning a value and printing to the console.
- **Variable Scope:** Demonstrating the boundaries between global and local variables.
- **Control Flow:** Understanding how the `return` statement immediately halts function execution.
- **Error Tracing:** Identifying `NoneType` errors caused by missing return statements.

### Section 2: Basic Algorithms
- **Custom Iterators:** Reverse countdown loops.
- **List Indexing:** Accessing specific indices and combining them with array metadata (length).
- **Dynamic List Generation:** Creating lists dynamically based on specified lengths and fill values.

## 🛠️ Tech Stack
- **Language:** Python 3.x

## 📋 Key Learnings

- **Unreachable Code:** Any code written after a `return` statement in the same code block is ignored.
- **Scoping Rules:** Variables assigned inside a function belong to that function's local scope unless specified otherwise. Reassigning a global variable inside a function does not change the global variable unless you return the value and reassign it outside.