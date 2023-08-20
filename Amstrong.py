
def Amstrong(n):
    n = str(n)
    n_len = len(n)

    val = [int(i) ** n_len for i in n ]
    if sum(val) == int(n):
        return True
    return False

print(Amstrong(153))
