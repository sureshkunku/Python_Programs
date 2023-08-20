

n = 5

for i in range(n):
    print(" "*(n-i), end="")
    print(" ".join(map(str, str(11**i))))
