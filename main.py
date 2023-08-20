def combination(lst, n):
    if n == 0:
        return [[]]

    if not lst:
        return []

    l = []
    for i in range(len(lst)):
        ele = lst[i]
        restel = lst[i + 1:]
        restcom = combination(restel, n - 1)
        for j in restcom:
            l.append([ele] + j)
    return l


lst = [1, 2, 3, 4]
print(combination(lst, 2))
