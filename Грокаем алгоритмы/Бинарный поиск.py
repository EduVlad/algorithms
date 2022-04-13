arr = [1, 2, 3, 5, 7, 9]


def binary_search(arr, elem):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem == arr[mid]:
            return mid
        if elem < arr[mid]:
            end = mid - 1
        else:   # elem > arr[mid]
            start = mid + 1
    return False


print(binary_search(arr, 7))  # => 1
print(binary_search(arr, -1))
