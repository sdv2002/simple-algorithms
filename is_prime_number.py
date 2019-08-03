def is_prime(num):
    """Prime check"""
    if num < 2:
        return False
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    return True


def prime_factorisation(n):
    """Is the decomposition of a composite number into a product
    of smaller integer prime numbers"""
    prime_numbers = []
    integers = []
    for i in range(n+1):
        if is_prime(i):
            prime_numbers.append(i)
    if n in prime_numbers:
        return f'{n} is prime'
    k = 0
    while k < len(prime_numbers):
        if n % prime_numbers[k] == 0:
            integers.append(prime_numbers[k])
            n //= prime_numbers[k]
        else:
            k += 1
    return integers


if __name__ == '__main__':
    print(prime_factorisation(38))
