import random
def randInt(min=None,max=None):
    if min is None and max is None:
        print("There is no min or max")
        min=0
        max=100
    elif min is None:
        print("There is just a max")
        min=0
    elif max is None:
        print("There is just a min")
        max=100
    else:
     print("There are min and max too")
    range_width = max - min
    num = random.random() * range_width + min  
    return round(num)       
print(randInt())              
print(randInt(max=20))          
print(randInt(min=20))          
print(randInt(min=20, max=50)) 