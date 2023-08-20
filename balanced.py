def is_balanced(expression):
    open_brackets = ['(', '[', '{']
    closed_brackets = [')', ']', '}']
    stack = []
    for char in expression:
        if char in open_brackets:
            stack.append(char)
        elif char in closed_brackets:
            if len(stack) == 0:
                return False
            else:
                last_opem_bracket = stack.pop()
                if open_brackets.index(last_opem_bracket) != closed_brackets.index(char):
                    return False
    return len(stack) == 0


# Testing the function
test_cases = ["({[()]})"]
for test_case in test_cases:
    if is_balanced(test_case):
        print(f"{test_case}: Balanced")
    else:
        print(f"{test_case}: Not balanced")
