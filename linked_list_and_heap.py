import random


class LinkedList:
    def __init__(self):
        self._begin = None

    def insert(self, e):
        self._begin = [e, self._begin]

    def pop(self):
        try:
            d = self._begin[0]
            self._begin = self._begin[1]
            return d
        except TypeError:
            print('List empty')
            return None


class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    def insert(self, element):
        self.values.append(element)
        self.size += 1
        self.sift_up(self.size - 1)

    def sift_up(self, i):
        while i != 0 and self.values[i] < self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = \
                self.values[(i - 1) // 2], self.values[i]
            i = (i - 1) // 2

    def extract_min(self):
        if not self.size:
            return None
        tmp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size -= 1
        self.sift_down(0)
        return tmp

    def sift_down(self, i):
        while i * 2 + 1 < self.size:
            j = i
            if self.values[i * 2 + 1] < self.values[i]:
                j = i * 2 + 1
            if i * 2 + 2 < self.size:
                if self.values[i * 2 + 2] < self.values[i * 2 + 1]:
                    j = i * 2 + 2
            if i == j:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j


def heap_sort(array):
    heap = Heap()
    # Slow version:
    # for i in range(len(array)):
    #    heap.insert(array.pop())
    #
    # Fast version:
    heap.values = array[:]
    heap.size = len(array)
    for i in reversed(range(heap.size // 2)):
        heap.sift_down(i)
    array = []
    # end fast version
    while heap.size:
        array.append(heap.extract_min())
    return array


if __name__ == '__main__':
    a = []
    for x in range(20):
        a.append(random.randint(0, 100))
    print(a)
    print(heap_sort(a))
