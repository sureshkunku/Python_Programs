

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    mer_arr = merge(left, right)
    return mer_arr

def merge(left, right):
    mer_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            mer_arr.append(left[i])
            i +=1
        else:
            mer_arr.append(right[j])
            j +=1
    mer_arr.extend(left[i:])
    mer_arr.extend(right[j:])
    return mer_arr

l = [1,6,3,8,2]
print(merge_sort(l))