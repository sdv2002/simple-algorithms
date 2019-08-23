def factorial(n):
    return 1 if n <= 1 else factorial(n - 1) * n


def euclidean(a, b):
    """Euclidean algorithm allows us to find
        the greatest common divisor of numbers"""

    # First variant:
    if a == b:
        return a
    elif a > b:
        return euclidean(a - b, b)
    else:
        return euclidean(b - a, a)

    # Second variant:
    # return a if b == 0 else euclidean(b, a % b)


def quick_exponentiation(a, n):
    """Exponentiating by squaring is a general method for fast
    computation of large positive integer powers of a number."""
    if n == 0:
        return 1
    elif n % 2 == 1:  # n: odd
        return quick_exponentiation(a, n - 1) * a
    else:  # n: even
        return quick_exponentiation(a ** 2, n // 2)


def hanoi_towers(n, a, b, c):
    if n != 0:
        hanoi_towers(n - 1, a, c, b)
        print(f'Transfer ring from {a} to {c}')
        hanoi_towers(n - 1, b, a, c)


def generate_binary_numbers(m: int, prefix=''):
    """Generates all numbers of length m in binary notation."""
    if m == 0:
        print(prefix, end=' ')
        return
    generate_binary_numbers(m-1, prefix+'0')
    generate_binary_numbers(m-1, prefix+'1')


def generate_numbers(n: int, m: int, prefix=None):
    """Generates all numbers in an n-ary (n <= 10) numeral system
    of length m."""
    prefix = prefix or []
    if m == 0:
        print(*prefix, sep='', end=' ')
        return
    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m - 1, prefix)
        prefix.pop()


def generate_permutations(n: int, m=None, prefix=None):
    """Generation of all permutations of n numbers in m positions."""
    m = n if m is None else m
    prefix = prefix or []
    if m == 0:
        print(*prefix, sep='', end=' ')
        return
    for number in range(1, n + 1):
        if number not in prefix:
            prefix.append(number)
            generate_permutations(n, m - 1, prefix)
            prefix.pop()


if __name__ == '__main__':
    generate_permutations(6)
