def number_to_words(num):
    single_digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if num == 0:
        return "zero"

    if num < 10:
        return single_digits[num]

    if num < 20:
        return teens[num - 10]

    if num < 100:
        tens_digit, remainder = divmod(num, 10)
        # tens_digit = num // 10
        # remainder = num % 10
        return tens[tens_digit] + " " + single_digits[remainder]

    if num < 1000:
        hundreds_digit = num // 100
        remainder = num % 100
        return single_digits[hundreds_digit] + " hundred " + number_to_words(remainder)

    return "one thousand"


num_word = number_to_words(3020)
print(num_word)

# for num in range(1, 1001):
#     num_word = number_to_words(num)
#     print(f"{num}: {num_word}")


##################################
# from num2words import num2words
#
# for num in range(1, 1001):
#     num_word = num2words(num)
#     print(f"{num}: {num_word}")

#
from permutations import print_permutations
#
# input = "abcb"
# print(print_permutations(input))

from itertools import permutations
input = "abcb"
for i in permutations(input, 4):
    print("".join(i))

