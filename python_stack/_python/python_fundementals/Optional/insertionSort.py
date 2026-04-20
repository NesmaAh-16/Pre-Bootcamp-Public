def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position = position - 1           

        arr[position] = current_value
    return arr

my_list = [12, 11, 13, 5, 6]
print(f"Original: {my_list}")

sorted_list = insertion_sort(my_list)
print(f"Sorted:   {sorted_list}")