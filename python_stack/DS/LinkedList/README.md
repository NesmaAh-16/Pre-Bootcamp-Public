
Python Singly Linked List implementation.
Singly Linked List Implementation (Python)

This project provides a robust implementation of a Singly Linked List in Python.
It includes standard operations like adding/removing from both ends, as well as
more advanced features like inserting at a specific index and removing the
n^{th} occurrence of a specific value.

🚀 Features

  - Efficient Insertions: Add to the front in O(1) time.
  - Flexible Removal: Remove by value, by position, or by the specific
    occurrence of a value.
  - Method Chaining: Most methods return self, allowing for fluent syntax (e.g.,
    list.add(1).add(2)).
  - Readable Display: A built-in visualization method to see the structure of
    your list.

🛠️ Methods Overview

Insertions

| Method              | Description                                   | Time Complexity |
| :------------------ | :-------------------------------------------- | :-------------- |
| `add_to_front(val)` | Adds a new node to the beginning of the list. | $O(1)$          |
| `add_to_back(val)`  | Adds a new node to the end of the list.       | $O(n)$          |
| `insert_at(val, n)` | Inserts a value at index `n` (0-indexed).     | $O(n)$          |

Deletions

| Method                | Description                                                          | Time Complexity |
| :-------------------- | :------------------------------------------------------------------- | :-------------- |
| `remove_from_front()` | Removes the first node.                                              | $O(1)$          |
| `remove_from_back()`  | Removes the last node.                                               | $O(n)$          |
| `remove_val(val)`     | Removes the **first** node found with the given value.               | $O(n)$          |
| `remove(val, n)`      | Removes the **$n^{th}$ occurrence** of a specific value (1-indexed). | $O(n)$          |

Utility

| Method      | Description                                            | Time Complexity |
| :---------- | :----------------------------------------------------- | :-------------- |
| `display()` | Prints the list in the format: `val1 -> val2 -> val3`. | $O(n)$          |

💻 Usage Example

from linked_list import LinkedList

# Initialize the list
ll = LinkedList()

# Using Method Chaining to build a list
ll.add_to_front("world").add_to_front("hello")
ll.display() 
# Output: hello -> world

# Inserting at a specific position
ll.insert_at("beautiful", 1)
ll.display()
# Output: hello -> beautiful -> world

# Removing the nth occurrence of a value
# List: 10 -> 20 -> 10 -> 30
nums = LinkedList()
nums.add_to_back(10).add_to_back(20).add_to_back(10).add_to_back(30)
nums.remove(10, 2) # Removes the second '10'
nums.display()
# Output: 10 -> 20 -> 30

🏗️ Data Structure Internal Logic

The Node Class

The building block of the list. Each node stores a value and a pointer (next) to
the succeeding node.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

The LinkedList Class

The manager of the nodes. It tracks the head (start) of the list. If the head is
None, the list is considered empty.
