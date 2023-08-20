def find_second_max(nums):
    # Initialize variables to track maximum and second maximum
    max_value = float('-inf')  # Initialize max_value to negative infinity
    second_max_value = float('-inf')  # Initialize second_max_value to negative infinity

    # Iterate over the list
    for num in nums:
        # Update max_value and second_max_value accordingly
        if num > max_value:
            second_max_value = max_value
            max_value = num
        elif num > second_max_value and num < max_value:
            second_max_value = num

    return second_max_value

# Example usage
nums = [10, 5, 8, 12, 3]
second_max = find_second_max(nums)
print(second_max)
