# Python Algorithms & Functional Utilities

This repository contains implementations of classic sorting algorithms and a custom functional programming library. These exercises demonstrate an understanding of time complexity, memory management, and higher-order functions.

## 🚀 Features

### 1. Sorting Algorithms
- **Insertion Sort:** An $O(n^2)$ algorithm that builds the final sorted array one item at a time. Efficient for small data sets or nearly sorted data.
- **Selection Sort:** An $O(n^2)$ in-place comparison sort. It is known for its simplicity and performance advantages over more complex algorithms in specific limited-memory situations.

### 2. Functional Programming Library (The Underscore Class)
A custom implementation of a utility library (inspired by Underscore.js) that demonstrates the power of **Lambda functions** and **Callbacks**.
- `.map()`: Transforms each element in a collection.
- `.find()`: Returns the first element that passes a truth test.
- `.filter()`: Returns all elements that pass a truth test.
- `.reject()`: The inverse of filter; returns all elements that fail a truth test.

## 🛠️ Technical Concepts
- **In-place Swapping:** Using Python’s `a, b = b, a` syntax for efficient memory usage.
- **Predicates:** Using callback functions that return booleans to drive logic.
- **Big O Notation:** Understanding the efficiency of nested loops.
- **Lambdas:** Utilizing anonymous functions for concise logic.

## 📋 Usage Example
```python
_ = Underscore()
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# Output: [2, 4, 6]