class Node:
    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item


class LinkedList:
    """Linked list is a linear collection of data elements,
    whose order is not given by their physical placement in memory.
    Instead, each element points to the next."""
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.length == 0:
            return 'Linked List: []'
        current = self.first
        out = f'Linked List: [{current.value}'
        while current is not None:
            current = current.next_item
            if current is not None:
                out += f' > {current.value}'
        return out + ']'

    def __iter__(self):
        current = self.first
        while current:
            yield current.value
            current = current.next_item

    def add(self, x):
        """Add item to end of list."""
        if self.first is None:
            self.first = Node(x)
            self.last = self.first
        elif self.first == self.last:
            self.last = Node(x)
            self.first.next_item = self.last
        else:
            current = Node(x)
            self.last.next_item = current
            self.last = current
        self.length += 1

    def push(self, x):
        """Add item to top of list."""
        if self.first is None:
            self.first = Node(x)
            self.last = self.first
        else:
            self.first = Node(x, self.first)
        self.length += 1

    def insert(self, x, i):
        """Adding the element x to the position at the index i."""
        if i > self.length:
            raise IndexError(f'list length is {self.length}')
        elif self.first is None:
            self.first = Node(x)
            self.last = self.first
        elif i == 0:
            self.first = Node(x, self.first)
        else:
            current = self.first
            count = 0
            while current is not None:
                if count == i - 1:
                    current.next_item = Node(x, current.next_item)
                    if current.next_item.next_item is None:
                        self.last = current.next_item
                    break
                current = current.next_item
                count += 1
        self.length += 1

    def pop(self):
        """Remove item from top of list."""
        old_head = self.first
        if old_head is None:
            return None
        self.first = old_head.next_item
        if self.first is None:
            self.last = None
        self.length -= 1
        return old_head.value

    def delete_by_index(self, i):
        """Remove an item from the list by index i."""
        if i >= self.length:
            raise IndexError(f'list length is {self.length}')
        elif self.first is None:
            return
        elif i == 0:
            self.first = self.first.next_item
        else:
            old = current = self.first
            count = 0
            while current is not None:
                if count == i:
                    if current.next_item is None:
                        self.last = old
                        break
                    else:
                        old.next_item = current.next_item
                    break
                old = current
                current = current.next_item
                count += 1
        self.length -= 1

    def search(self, x):
        """Search for the item x in the list."""
        if self.length == 0:
            return None
        current = self.first
        i = 0
        while current is not None:
            if current.value == x:
                return i
            current = current.next_item
            i += 1
        return None

    def delete_by_value(self, x):
        i = self.search(x)
        if i is None:
            return
        self.delete_by_index(i)

    def reverse(self):
        """Invert linked list"""
        if self.length < 2:
            return
        previous = None
        current = self.first
        self.last = current
        while current is not None:
            nex = current.next_item
            current.next_item = previous
            previous = current
            current = nex
        self.first = previous


def loop_search(linked_list: LinkedList):
    """Searches for a loop in a linked list."""
    slow = linked_list.first
    fast = linked_list.first
    step = 0
    while fast is not None:
        if fast.next_item is None or fast.next_item.next_item is None:
            print('No loop')
            return
        fast = fast.next_item.next_item
        slow = slow.next_item
        step += 1
        if slow == fast:
            break
    slow = linked_list.first
    while slow != fast:
        fast = fast.next_item
        slow = slow.next_item
    print(f'Loop start: {slow.value}')


if __name__ == '__main__':
    a = LinkedList()
    a.add('a')
    a.add('b')
    a.add('c')
    a.add('d')
    a.add('e')
    a.add('f')
    # a.first.next_item.next_item.next_item.next_item.next_item = \
    #     a.first.next_item.next_item
    # print(a)
    loop_search(a)
    s = 20
    for item in a:
        print(item, end=' ')
        s -= 1
        if not s:
            break
