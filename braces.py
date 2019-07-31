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


if __name__ == '__main__':
    print(is_brackets_correct('[([)]]'))