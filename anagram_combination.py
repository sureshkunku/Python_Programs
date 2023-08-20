strs = ['abcd', 'adbc', 'cabd', 'def', 'pqr', 'qpr']

# output = [['def'], ['pqr',   'qpr'], ['abcd', 'adbc', 'cabd']]
import string
from collections import defaultdict
def anagram(strs):
    d = defaultdict(list)
    for i in strs:
        l = [0] * 26
        for j in i:
            l[ord(j) - ord('a')] = 1
        key = tuple(l)
        d[key].append(i)
    return d.values()
print(anagram(strs))