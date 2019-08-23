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
    a[:] = left + middle + right


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


def merge(left: list, right: list):
    """Merging sorted arrays."""
    i = j = n = 0
    result = [0] * (len(left) + len(right))
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result[n] = left[i]
            i += 1
        else:
            result[n] = right[j]
            j += 1
        n += 1
    while i < len(left):
        result[n] = left[i]
        i += 1
        n += 1
    while j < len(right):
        result[n] = right[j]
        j += 1
        n += 1
    return result


if __name__ == '__main__':
    arr1 = [x for x in range(20)]
    random.shuffle(arr1)
    arr2 = [x for x in range(20)]
    random.shuffle(arr2)
    print(arr1, arr2)

    quick_sort(arr1)
    merge_sort(arr2)
    print(arr1, arr2)
