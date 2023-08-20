def prime_factorization(n):
    factors = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        else:
            divisor += 1

    return factors

# Example usage
number = 84
factors = prime_factorization(number)

print(f"The prime factors of {number} are: {factors}")
