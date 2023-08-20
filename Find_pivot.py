
def find_pivot(l):
    tol_sum = sum(l)
    lef_sum = 0
    for i in range(len(l)):
        tol_sum = tol_sum - l[i]
        if tol_sum == lef_sum:
            return i
        lef_sum += l[i]
    return -1

l  = [1, 7, 3, 6, 5, 6]

print(find_pivot(l))