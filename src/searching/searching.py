def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    zero_index = 0
    end_index = len(arr) - 1

    while zero_index <= end_index:
        middle_index = zero_index + end_index // 2 
        if target == arr[middle_index]:
            return middle_index
        if target > arr[middle_index]:
            zero_index = middle_index + 1
        else:
            end_index = middle_index - 1

    return -1  # not found
