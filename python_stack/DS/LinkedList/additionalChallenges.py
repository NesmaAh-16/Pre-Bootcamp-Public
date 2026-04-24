class Node:
    def __init__(self, value):
        self.value = value # Consistent naming
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = Node(val) # Changed SLNode to Node
        new_node.next = self.head
        self.head = new_node
        return self

    def add_to_back(self, val):
        if self.head is None:
            return self.add_to_front(val)
        new_node = Node(val) # Changed SLNode to Node
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        if self.head:
            self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head is None:
            return self
        if self.head.next is None:
            self.head = None
            return self
        
        runner = self.head
        while runner.next.next:
            runner = runner.next
        runner.next = None
        return self

    def remove_val(self, val):
        if not self.head:
            return self
        if self.head.value == val:
            return self.remove_from_front()
        
        runner = self.head
        while runner.next:
            if runner.next.value == val:
                runner.next = runner.next.next
                return self
            runner = runner.next
        return self

    def insert_at(self, val, n):
        if n < 0: return self
        if n == 0: return self.add_to_front(val)
        
        new_node = Node(val)
        runner = self.head
        count = 0
        while runner and count < n - 1:
            runner = runner.next
            count += 1
        
        if runner:
            new_node.next = runner.next
            runner.next = new_node
        return self
    
    def remove(self, val, n):
        """Removes the nth occurrence of the given value (n is 1-indexed)."""
        if self.head is None or n <= 0:
            return self

        occurrence_count = 0

        # 1. Check if the head is the node to remove
        if self.head.value == val:
            occurrence_count += 1
            if occurrence_count == n:
                self.head = self.head.next
                return self

        # 2. Search through the rest of the list
        runner = self.head
        while runner.next:
            if runner.next.value == val:
                occurrence_count += 1
                if occurrence_count == n:
                    # Found the nth occurrence! Bypass it.
                    runner.next = runner.next.next
                    return self
            runner = runner.next
        
        print(f"Occurrence {n} of value '{val}' not found.")
        return self
    
    def display(self):
        """Prints the list in a readable format."""
        runner = self.head
        output = []
        while runner:
            output.append(str(runner.value))
            runner = runner.next
        print(" -> ".join(output) if output else "Empty List")

# --- Testing ---

ll = LinkedList()
print("--- Testing Inserts ---")
ll.insert_at(10, 0) 
ll.insert_at(30, 1) 
ll.insert_at(20, 1) 
ll.display() # Expected: 10 -> 20 -> 30

print("\n--- Testing Removal ---")
ll.remove_val(10) # Remove head
ll.display() # Expected: 20 -> 30
ll.remove(20, 2)
ll.display()
ll.add_to_back(40)
ll.remove_val(40) # Remove tail
ll.display() # Expected: 20 -> 30

print("\n--- Testing Method Chaining ---")
my_list = LinkedList()
my_list.add_to_front("are").add_to_front("Lists").add_to_back("fun!").add_to_front("Linked")
my_list.display() # Expected: Linked -> Lists -> are -> fun!