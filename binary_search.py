def binary_search(a, key):
    """searching for the element key in a sorted array a."""
    left = -1
    right = len(a)
    while (right - left) > 1:
        middle = (right + left) // 2
        if key < a[middle]:
            right = middle
        elif key > a[middle]:
            left = middle
        else:
            return middle
    return


if __name__ == '__main__':
    print(binary_search([3, 5, 5, 5, 15], 5))