def second_min(array):
    """Search for the second minimum value in an array. O(n)"""
    for i in range(2, len(array)):
        if array[i] < array[0]:
            tmp = array[0]
            array[0] = array[i]
            array[i] = tmp
        if array[i] < array[1]:
            array[1] = array[i]
    return array[1]


def non_repeat(array):
    """Search the first non-repeating integers in an array. O(n)"""
    result = []
    for i in range(len(array) - 1):
        if array[i + 1] == array[i]:
            continue
        result.append(array[i + 1])
    return result


def reordering(array):
    """Reordering positive and negative values in an array."""
    negative = []
    positive = []
    while array:
        x = array.pop()
        if x < 0:
            negative.append(x)
        else:
            positive.append(x)
    negative.reverse()
    positive.reverse()
    return negative + positive


def invert(array):
    """Revers the list"""
    length = len(array)
    for i in range(length // 2):
        array[i], array[length - i - 1] = array[length - i - 1], array[i]
    return array


if __name__ == '__main__':
    a = [1, 2, -10, 5, -20, 3, -30]
    print(reordering(a))
