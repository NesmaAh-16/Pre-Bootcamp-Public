#1
def countDown(num):
    for x in range(num,0,-1):
        print(x)
countDown(5)
        
#2
def print_and_return(my_list):
    print(my_list[0]) 
    return my_list[len(my_list)-1] 
x=print_and_return([1,2])
print(x)


#3
def first_plus_length(my_list):
    return my_list[0] + len(my_list)


#4 
def values_greater_than_second(my_list):
    if len(my_list) < 2:
        return False
    new_list = []
    second_val = my_list[len(my_list)]   
    for x in my_list:
        if x > second_val:
            new_list.append(x)
            
    print(len(new_list)) 
    return new_list     

#5
def length_and_value(size, value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list
