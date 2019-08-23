import time
import random


def insertion_sort(array):
    """Insertion sort. O(n**2)"""
    for top in range(1, len(array)):
        k = top
        while k > 0 and array[k - 1] > array[k]:
            array[k - 1], array[k] = array[k], array[k - 1]
            k -= 1
    return array


def selection_sort(array):
    """Selection sort. O(n**2)"""
    for x in range(len(array)):
        index_min_el = x
        for pos in range(x + 1, len(array)):
            if array[pos] < array[index_min_el]:
                index_min_el = pos
        array[x], array[index_min_el] = array[index_min_el], array[x]
    return array


def bubble_sort(array):
    """Bubble sort. O(n**2)"""
    for pos in range(len(array)-1):
        for x in range(len(array)-pos-1):
            if array[x] > array[x+1]:
                array[x], array[x+1] = array[x+1], array[x]
    return array


if __name__ == '__main__':
    m = [x for x in range(10000)]
    random.shuffle(m)
    start = time.monotonic()
    insertion_sort(m)
    end = time.monotonic()
    print(end - start)
