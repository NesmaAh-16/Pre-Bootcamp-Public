class Queue:
    def __init__(self):
        self.items = []
        self.head = 0 # first position

    def enqueue(self, x):
        self.items = self.items + [x]

    def dequeue(self):
        if len(self.items) == 0:
            return None 
        
        item = self.items[0]
        self.items = self.items[1:] 
        return item

    def front(self):
        if self.head >= len(self.items):
            return None
        return self.items[self.head]
q = Queue()

q.enqueue("Asma")
q.enqueue("Dania")
q.enqueue("Nesma")

print(q.front())   #asma
print( q.dequeue()) #asma
print( q.front()) #dania
print("Remain in queue:", q.items) # [ ]
print(ord("ل"))