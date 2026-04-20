def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

numbers_list = [64, 25, 12, 22, 11]
print(f"Original list: {numbers_list}")
sorted_list = selection_sort(numbers_list)
print(f"Sorted list:   {sorted_list}")