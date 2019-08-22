from collections import deque


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


if __name__ == '__main__':
    a = StackThroughQueue()
    a.push(1)
    a.push(2)
    a.push(3)
    a.push(4)
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
    print(a.pop())
