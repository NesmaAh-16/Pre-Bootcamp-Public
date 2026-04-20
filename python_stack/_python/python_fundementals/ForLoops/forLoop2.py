# 1
def biggie_size(my_list):
    for i in range(len(my_list)):
        if my_list[i] > 0:
            my_list[i] = "big"
    return my_list

# 2
def count_positives(my_list):
    count = 0
    for val in my_list:
        if val > 0:
            count += 1
    my_list[len(my_list)-1] = count
    return my_list

# 3
def sum_total(my_list):
    total = 0
    for val in my_list:
        total += val
    return total

# 4
def average(my_list):
    total = 0
    for val in my_list:
        total += val
    return total / len(my_list)

# 5
def length(my_list):
    return len(my_list)

# 6
def minimum(my_list):
    if len(my_list) == 0:
        return False
    min_val = my_list[0]
    for val in my_list:
        if val < min_val:
            min_val = val
    return min_val

# 7
def maximum(my_list):
    if len(my_list) == 0:
        return False
    max_val = my_list[0]
    for val in my_list:
        if val > max_val:
            max_val = val
    return max_val

# 8
def ultimate_analysis(my_list):
    analysis = {
        'sumTotal': sum_total(my_list),
        'average': average(my_list),
        'minimum': minimum(my_list),
        'maximum': maximum(my_list),
        'length': length(my_list)
    }
    return analysis

# 9
def reverse_list(my_list):
    left = 0
    right = len(my_list) - 1
    while left < right:
        my_list[left], my_list[right] = my_list[right], my_list[left]
        left += 1
        right -= 1
    return my_list