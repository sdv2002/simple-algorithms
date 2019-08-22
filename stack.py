from queue import Queue


class StackThroughQueue:
    """Implementing a stack using a queue."""
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        if self.q1.empty():
            self.q1.put(x)
            while not self.q2.empty():
                self.q1.put(self.q2.get())
        else:
            self.q2.put(x)
            while not self.q1.empty():
                self.q2.put(self.q1.get())

    def pop(self):
        if not self.q1.empty():
            return self.q1.get()
        elif not self.q2.empty():
            return self.q2.get()
        else:
            return None


def is_brackets_correct(string):
    """Checking the correctness of the bracket sequence."""
    stack = []
    for character in string:
        if character not in '()[]':
            continue
        elif character in '([':
            stack.append(character)
        else:
            assert character in ')]', 'Expected closing bracket.'
            if len(stack) == 0:
                return False
            left = stack.pop()
            right = ')' if left == '(' else ']'
            if right != character:
                return False
    return True if len(stack) == 0 else False


def sort_stack(stack):
    """Sort values on the stack. O(n**2)"""
    temp_stack = []
    while stack:
        x = stack.pop()
        while temp_stack and temp_stack[-1] > x:
            stack.append(temp_stack.pop())
        temp_stack.append(x)
    return temp_stack


def revers_string(array):
    """Reverse a string using a stack"""
    stack = []
    while array:
        stack.append(array.pop())
    return stack


if __name__ == '__main__':
    a = [3, 2, 10, 0, 7]
    print(revers_string(a))
