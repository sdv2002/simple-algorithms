class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinarySearchTree:
    """A binary search tree is a rooted binary tree, whose internal nodes
    each store a key and each have two distinguished sub-trees,
    commonly denoted left and right. The tree additionally satisfies
    the binary search property, which states that the key in each node must
    be greater than or equal to any key stored in the left sub-tree,
    and less than or equal to any key stored in the right sub-tree."""
    def __init__(self):
        self.root = None
        self.length = 0

    def __str__(self):
        if self.length == 0:
            return 'Tree is empty.'
        array = []
        x = self.root
        self.inorder_traversal(x, array)
        return str(array)

    def inorder_traversal(self, x, array):
        if x is not None:
            self.inorder_traversal(x.left, array)
            array.append(x.key)
            self.inorder_traversal(x.right, array)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            self.length += 1
            return
        x = self.root
        self.recursive_insert(x, key)
        self.length += 1

    def recursive_insert(self, x, key):
        if x is None:
            return Node(key)
        if key < x.key:
            x.left = self.recursive_insert(x.left, key)
        if key > x.key:
            x.right = self.recursive_insert(x.right, key)
        return x


if __name__ == '__main__':
    a = BinarySearchTree()
    print(a)
    a.insert(5)
    print(a, a.root.key, a.root.left, a.root.right)
    a.insert(9)
    a.insert(2)
    a.insert(4)
    print(a)
    print(a.root.left.right.key)
