# def Fibona(num):
#     a = 0
#     b = 1
#
#     print(a, b)
#
#     for i in range(num - 2):
#         c = a + b
#         a = b
#         b = c
#         print(c, end=" ")
#

def Fibona(num):
    a = 0
    b = 1
    print(a, b)
    for i in range(num - 2):
        c = a + b
        a = b
        b = c
        return Fibona(c, end=" ")

print(Fibona(10))

def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Test the function
num_terms = 10
for i in range(1, num_terms + 1):
    print(f"Fibonacci term {i}: {fibonacci_recursive(i)}")
