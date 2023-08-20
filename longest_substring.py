def longest_substring(string):
    unique_string = set()
    right = 0
    left = 0
    max_length = 0
    longest_substring = ""

    while right < len(string):
        if string[right] not in unique_string:
            unique_string.add(string[right])
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                longest_substring = string[left: right + 1]
            right += 1
        else:
            unique_string.remove(string[left])
            left += 1
    return longest_substring


# Testing the function
input_string = "greeksforkeek"
result = longest_substring(input_string)
print("Longest Substring:", result)
print("Length:", len(result))
