

def prime(n):
    l = []
    if n <= 0:
        return -1
    count = 2
    while len(l) < 10:
        check = 0
        if count == 4:
            count += 1
            continue
        for i in range(2, count//2):
            if count % i == 0:
                check +=1
        if check == 0:
            l.append(count)
        count += 1

    return l

print(prime(10))

def nth_prime_number(n):
    if n <= 0:
        return None

    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True

        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

        num += 1

    return primes

# Example usage
n = 10
nth_prime = nth_prime_number(n)
print(nth_prime)


################

def nth_prime_number(n):
    if n <= 0:
        return None

    primes = []
    num = 2

    while len(primes) < n:
        is_prime = True

        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

        num += 1

    return primes[-1]

# Example usage
n = 10
nth_prime = nth_prime_number(n)
print(f"The {n}th prime number is: {nth_prime}")

