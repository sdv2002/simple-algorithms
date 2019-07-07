def invert(num_list):
    """Revers the list"""
    length = len(num_list)
    for i in range(length//2):
        num_list[i], num_list[length-i-1] = num_list[length-i-1], num_list[i]
    return num_list


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print(invert(a))
