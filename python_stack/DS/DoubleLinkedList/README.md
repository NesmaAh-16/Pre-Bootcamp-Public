Doubly Linked List Implementation 

This repository contains a Python implementation of a Doubly Linked List (DLL).
Unlike a singly linked list, each node in a doubly linked list contains a
reference to both the next node and the previous node. This allows for
bi-directional traversal and more flexible data manipulation.

🚀 Features

  - Bi-directional Navigation: Nodes can be traversed both forward and backward.
  - Efficient Front Operations: Adding and removing from the start occurs in
    O(1) time.
  - Robust Edge Case Handling: Methods account for empty lists and single-node
    lists.
  - Clean Traversal: Built-in methods to visualize the list in either direction.

🛠️ Methods Overview

Insertions

| Method            | Description                                           | Time Complexity |
| :---------------- | :---------------------------------------------------- | :-------------- |
| `add_start(data)` | Inserts a new node at the very beginning of the list. | $O(1)$          |
| `append(data)`    | Inserts a new node at the very end of the list.       | $O(n)$          |

Deletions

| Method           | Description                                      | Time Complexity |
| :--------------- | :----------------------------------------------- | :-------------- |
| `delete_start()` | Removes the first node and updates the head.     | $O(1)$          |
| `delete_end()`   | Removes the last node after traversing the list. | $O(n)$          |

Display & Traversal

| Method                | Description                                                  | Time Complexity |
| :-------------------- | :----------------------------------------------------------- | :-------------- |
| `traverse_forward()`  | Prints the list from head to tail.                           | $O(n)$          |
| `traverse_backward()` | Prints the list from tail to head using the `prev` pointers. | $O(n)$          |

💻 Usage Example

from doubly_linked_list import DoublyLinkedList

# 1. Initialize the list
dll = DoublyLinkedList()

# 2. Add elements
dll.append(10)      # List: 10
dll.append(20)      # List: 10 -> 20
dll.add_start(5)    # List: 5 -> 10 -> 20

# 3. Traversal
print("Forward:")
dll.traverse_forward()  # 5 -> 10 -> 20 -> None

print("Backward:")
dll.traverse_backward() # 20 -> 10 -> 5 -> None

# 4. Deletions
dll.delete_start()  # Removes 5
dll.delete_end()    # Removes 20
dll.traverse_forward() # 10 -> None

🏗️ Technical Logic

The Node Class

The Node class is the fundamental unit of the list. It contains three
attributes:

  - data: The value stored in the node.
  - next: A pointer to the next node (or None).
  - prev: A pointer to the previous node (or None).

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

The DoublyLinkedList Class

This class manages the head pointer. In a DLL, updating pointers is a two-step
process: when you link Node A to Node B, you must set A.next = B and B.prev = A.
This implementation ensures these links are always kept in sync to prevent
broken chains.
