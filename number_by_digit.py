def numbering(base, num):
    """Decomposes the number into digits in the number system with a base"""
    digits = []
    num = abs(num)
    while num != 0:
        digits.append(num % base)
        num //= base
    digits.reverse()
    return digits


if __name__ == '__main__':
    b = int(input('Enter the base of the number system: '))
    n = int(input('Enter number: '))
    print(numbering(b, n))
