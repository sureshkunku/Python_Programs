# def find_combinations(l, target_sum):
#     combinations = []
#     stack = [(0, [], 0)]
#
#     while stack:
#         current_sum, current_combination, start = stack.pop()
#
#         if current_sum == target_sum:
#             combinations.append(current_combination)
#             continue
#
#         for i in range(start, len(l)):
#             num = l[i]
#             new_sum = current_sum + num
#
#             if new_sum <= target_sum:
#                 stack.append((new_sum, current_combination + [num], i))
#
#     return combinations
#
#
# # Test the function
# l = [2, 3, 5]
# target_sum = 8
# result = find_combinations(l, target_sum)
# print(result)

############################

def find_combinations(l, target_sum):
    result = []
    combination = []
    backtrack(l, target_sum, 0, combination, result)
    return result

def backtrack(l, target_sum, start, combination, result):
    if target_sum == 0:
        result.append(combination[:])
        return
    if target_sum < 0:
        return
    for i in range(start, len(l)):
        num = l[i]
        combination.append(num)
        backtrack(l, target_sum - num, i, combination, result)
        combination.pop()

# Test the function
l = [2, 3, 5]
target_sum = 8
result = find_combinations(l, target_sum)
print(result)
