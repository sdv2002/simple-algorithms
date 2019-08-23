from collections import deque
from math import log2


class StackThroughQueue:
    """Implementing a stack using a queue."""
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        if not self.q1:
            self.q1.append(x)
            while self.q2:
                self.q1.append(self.q2.popleft())
        else:
            self.q2.append(x)
            while self.q1:
                self.q2.append(self.q1.popleft())

    def pop(self):
        if self.q1:
            return self.q1.popleft()
        elif self.q2:
            return self.q2.popleft()
        else:
            return None


def transposition(queue: deque, k):
    """Rearranges the first k elements of the queue."""
    for _ in range(k):
        queue.appendleft(queue.pop())


def generate_binary_numbers(n):
    """Generate binary numbers from 1 to n using a queue."""
    digits = int(log2(n)) + 1
    list_of_numbers = []
    for x in range(1, n + 1):
        queue = deque()
        while x:
            queue.appendleft(str(x % 2))
            x = x // 2
        binary = ''.join(list(queue))
        list_of_numbers.append('0' * (digits - len(binary)) + binary)
    return list_of_numbers


if __name__ == '__main__':
    print(generate_binary_numbers(19))
