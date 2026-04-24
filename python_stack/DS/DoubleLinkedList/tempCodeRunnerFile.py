class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # add end 
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    # add start
    def add_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current=self.head
        self.head = new_node
        new_node.next = current
        
        

    #remove start
    def delete_start(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        if self.head.next is None: 
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    #remove end 
    def delete_end(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        if self.head.next is None: 
            self.head = None
            return
        
        temp = self.head
        while temp.next: 
            temp = temp.next
        
        temp.prev.next = None
        temp.prev = None

    # forward traversal 
    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # backward traversal 
    def traverse_backward(self):
        temp = self.head
        if not temp:
            print("List is empty!")
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("None")


dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
dll.add_start(5) 
dll.traverse_forward() 
dll.delete_start()
dll.traverse_forward() 
dll.delete_end()
dll.traverse_forward() 
dll.traverse_backward() 