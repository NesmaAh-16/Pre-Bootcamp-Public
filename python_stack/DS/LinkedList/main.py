class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None

    # add to the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # add to start
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # remove from start
    def delete_start(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        self.head = self.head.next

    # remove from the end
    def delete_end(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # Forward traversal
    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def traverse_backward(self):
        if not self.head:
            print("List is empty!")
            return
        
        def _recursive_print(node):
            if node is None:
                return
            _recursive_print(node.next) 
            print(node.data, end=" -> ") 

        _recursive_print(self.head)
        print("None")


sll = LinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.prepend(5) 
sll.traverse_forward() 
sll.delete_start()
sll.traverse_forward() 
sll.delete_end()
sll.traverse_forward() 
sll.traverse_backward() 