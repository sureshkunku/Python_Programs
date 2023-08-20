def binary_search(arr, target):
    if not arr:
        return -1

    left = 0
    right = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [5, 3, 8, 4, 2, 9, 1]
arr.sort()
target = 4
print(arr)
index = binary_search(arr, target)
print(index)
