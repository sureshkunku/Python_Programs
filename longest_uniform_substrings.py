def longest_uniform_substring(s):
    max_legnth = 1
    start = 0
    max_start = 0
    lenth = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            lenth += 1
        else:
            if max_legnth < lenth:
                max_legnth = lenth
                max_start = start

            start = i + 1
            lenth = 1

    if max_legnth < lenth:
        max_legnth = lenth
        max_start = start

    return [max_start, max_legnth]


# Example usage
string = "aabbcccccccc"
result = longest_uniform_substring(string)
print(result)
