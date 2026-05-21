class Stack:
    def __init__(self):
        self.elems=[]
    def push(self,x):
        self.elems=self.elems+ [x]
    def pop(self):
        if len(self.elems)==0:
            return None
        last_index=len(self.elems)-1
        top_item=self.elems[last_index]
        self.elems = self.elems[:last_index]
        return top_item
    def peek(self):
        if len(self.elems) == 0:
            return None
            
        last_index = len(self.elems) - 1
        return self.elems[last_index]

def reverse_string(text):
    s=Stack()
    for char in text:
        s.push(char)
    reversed_text=""
    while len(s.elems) > 0:
        reversed_text += s.pop()
    return reversed_text

original="Daina"
print(reverse_string(original))


def daily_tempreture(temps):
    n=len(temps)
    output=[0]*n #output[] len=len(temps) n
    stack_days=[]
    for i in range(n):
        while len(stack_days)>0 and temps[i] > temps[stack_days[-1]] :
            index=stack_days.pop()
            output[index]=i-index
        stack_days.append(i)
    return output

print(daily_tempreture([22,18,28,32,26,20,23]))

my_stack=Stack()
print("pushing elements: 90,40,60")
my_stack.push(90)
my_stack.push(40)
my_stack.push(60)
print("Top element is:", my_stack.peek()) 
my_stack.pop()
print("Top element is:", my_stack.peek())

