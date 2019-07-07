def is_prime(num):
    """Prime check"""
    if num < 2:
        return False
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    return True


if __name__ == '__main__':
    for n in range(0, 10):
        print('Num: ', n, ' is prime: ', is_prime(n))
