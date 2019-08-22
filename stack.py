class QueueThroughStack:
    """Implementing a queue using a stack."""
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, x):
        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())
        self.stack_1.append(x)
        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

    def dequeue(self):
        if self.stack_1:
            return self.stack_1.pop()


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
    """Reverse a string using a stack."""
    stack = []
    while array:
        stack.append(array.pop())
    return stack


def conversion_to_postfix(string):
    """Conversion from infix to postfix form."""
    operators_priority = {'*': 3,
                          '/': 3,
                          '+': 2,
                          '-': 2,
                          '(': 1
                          }
    stack = []
    postfix_list = []
    infix_list = string.split()
    for token in infix_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token.isdigit():
            postfix_list.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            operand = stack.pop()
            while operand != '(':
                postfix_list.append(operand)
                operand = stack.pop()
        elif token in operators_priority:
            if stack:
                operand = stack.pop()
                if operators_priority[operand] >= operators_priority[token]:
                    postfix_list.append(operand)
                else:
                    stack.append(operand)
            stack.append(token)
    while stack:
        postfix_list.append(stack.pop())
    return ' '.join(postfix_list)


def calculation_postfix(string):
    """Calculation an expression in postfix form."""
    stack = []
    postfix_list = string.split()
    for token in postfix_list:
        if token.isdigit():
            stack.append(int(token))
        if token in '*/+-':
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            stack.append(compute(operand_1, operand_2, token))
    return stack.pop()


def compute(x, y, operator):
    if operator == '*':
        return x * y
    elif operator == '/':
        return x / y
    elif operator == '+':
        return x + y
    else:
        return x - y


if __name__ == '__main__':
    q = QueueThroughStack()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
