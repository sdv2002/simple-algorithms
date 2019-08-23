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


def gen_bin(m, prefix=''):
    if m == 0:
        print(prefix)
        return
    gen_bin(m-1, prefix+'0')
    gen_bin(m-1, prefix+'1')


def generate_number(n: int, m: int, prefix=None, list_numbers=None):
    """Generates all numbers in an n-ary (n <= 10) numeral system
    of length m."""
    prefix = prefix or []
    list_numbers = list_numbers or []
    if m == 0:
        list_numbers.append(''.join(prefix))
        return list_numbers
    for digit in range(n):
        prefix.append(str(digit))
        generate_number(n, m - 1, prefix, list_numbers)
        prefix.pop()


if __name__ == '__main__':
    gen_bin(2)
    print(generate_number(2, 2))
