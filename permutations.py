def print_permutations(word):
    permute_helper(list(word), 0, len(word) - 1)

def permute_helper(word_list, left, right):
    if left == right:
        print("".join(word_list))
    else:
        for i in range(left, right + 1):
            word_list[left], word_list[i] = word_list[i], word_list[left]
            permute_helper(word_list, left + 1, right)
            word_list[left], word_list[i] = word_list[i], word_list[left]  # backtrack

# # Example usage
word = "abc"
# print_permutations(word)
# from itertools import permutations
# val = permutations(word, 2)
# for i in val:
#     print("".join(i))

# from itertools import permutations
# input = "abcb"
# for i in permutations(input, 4):
#     print("".join(i))

# l = [1,[3,[4,[5,[3,23]]]]]
#
# res = []
# def falt_list(l):
#     for i in l:
#         if isinstance(i, list):
#             falt_list(i)
#         else:
#             res.append(i)
#     return res
#
# print(falt_list(l))


# with recurive method
def generate_permutations(elements, r, current_permutation=[]):
    if len(current_permutation) == r:
        yield tuple(current_permutation)
    else:
        for element in elements:
            if element not in current_permutation:
                current_permutation.append(element)
                yield from generate_permutations(elements, r, current_permutation)
                current_permutation.pop()

# Example usage
elements = ['A', 'B', 'C']
r = 3

permutations_list = list(generate_permutations(elements, r))

for perm in permutations_list:
    print("".join(perm))

# without recursive method

def generate_permutations(elements):
    n = len(elements)
    c = [0] * n
    result = [elements[:]]

    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                elements[0], elements[i] = elements[i], elements[0]
            else:
                elements[c[i]], elements[i] = elements[i], elements[c[i]]
            result.append(elements[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1

    return result

# Example usage
elements = ['A', 'B', 'C']
permutations_list = generate_permutations(elements)

for perm in permutations_list:
    print("".join(perm))
