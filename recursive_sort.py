import random


def quick_sort(a):
    """Sorting algorithm by Tony Hoare. O(n log n)"""
    if len(a) <= 1:
        return
    barrier = a[0]
    left, middle, right = [], [], []
    for x in a:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    quick_sort(left)
    quick_sort(right)
    k = 0
    for x in left + middle + right:
        a[k] = x
        k += 1


def merge_sort(a):
    """Merge sort is an efficient, general-purpose,
        comparison-based sorting algorithm. O(n log n)"""
    if len(a) <= 1:
        return
    middle = len(a) // 2
    left = a[:middle]
    right = a[middle:len(a)]
    merge_sort(left)
    merge_sort(right)
    a[:] = merge(left, right)


def merge(arr_a: list, arr_b: list):
    """Merging sorted arrays."""
    i = k = n = 0
    arr_c = [0] * (len(arr_a) + len(arr_b))
    while i < len(arr_a) and k < len(arr_b):
        if arr_a[i] <= arr_b[k]:
            arr_c[n] = arr_a[i]
            i += 1
        else:
            arr_c[n] = arr_b[k]
            k += 1
        n += 1
    while i < len(arr_a):
        arr_c[n] = arr_a[i]
        i += 1
        n += 1
    while k < len(arr_b):
        arr_c[n] = arr_b[k]
        k += 1
        n += 1
    return arr_c


if __name__ == '__main__':
    arr1 = [x for x in range(20)]
    random.shuffle(arr1)
    arr2 = [x for x in range(20)]
    random.shuffle(arr2)
    print(arr1, arr2)

    quick_sort(arr1)
    merge_sort(arr2)
    print(arr1, arr2)
