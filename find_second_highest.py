

def find_second_highest(arr):
    max_val = arr[0]
    second_max = arr[0]

    for i in arr:
        if i > max_val:
            second_max = max_val
            max_val = i
        if i < max_val and i > second_max:
            second_max = i

    return second_max

arr = [20,30,20,10,40,60]

print(find_second_highest(arr))