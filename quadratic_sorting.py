def insertion_sort(array):
    """Insertion sort"""
    for top in range(1, len(array)):
        k = top
        while k > 0 and array[k - 1] > array[k]:
            array[k - 1], array[k] = array[k], array[k - 1]
            k -= 1
    return array


def selection_sort(array):
    """Selection sort"""
    for x in range(len(array)):
        index_min_el = x
        for pos in range(x + 1, len(array)):
            if array[pos] < array[index_min_el]:
                index_min_el = pos
        array[x], array[index_min_el] = array[index_min_el], array[x]
    return array


def bubble_sort(array):
    """Bubble sort"""
    for pos in range(len(array)-1):
        for x in range(len(array)-pos-1):
            if array[x] > array[x+1]:
                array[x], array[x+1] = array[x+1], array[x]
    return array


if __name__ == '__main__':
    print(bubble_sort([4, -2, -3, 2, 5, -3, 1]))
