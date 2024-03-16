class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def width_invert(self):
        the_current = [self]
        the_next = []
        while the_current:
            for node in the_current:
                if node.left_child:
                    the_next.append(node.left_child)
                if node.right_child:
                    the_next.append(node.right_child)
                tmp = node.left_child
                node.left_child = node.right_child
                node.right_child = tmp
            the_current = the_next
            the_next = []

    def has_leaf_node(self, value):
        the_current = [self]
        the_next = []
        while the_current:
            for node in the_current:
                if node.key == value:
                    if node.right_child is not None:
                        if node.right_child.right_child is None and node.right_child.left_child is None:
                            return True
                    if node.left_child is not None:
                        if node.left_child.right_child is None and node.left_child.left_child is None:
                            return True
                    return False
                if node.left_child:
                    the_next.append(node.left_child)
                if node.right_child:
                    the_next.append(node.right_child)
            the_current = the_next
            the_next = []
        return False


def inorder(a_tree):
    if a_tree:
        inorder(a_tree.left_child)
        print(a_tree.key, end=" ")
        inorder(a_tree.right_child)


def deep_invert(a_tree):
    if a_tree:
        tmp = a_tree.left_child
        a_tree.left_child = a_tree.right_child
        a_tree.right_child = tmp
        deep_invert(a_tree.left_child)
        deep_invert(a_tree.right_child)


tree = BinaryTree(5)
tree.insert_left(1)
tree.insert_left(2)
tree.left_child.insert_right(3)
tree.insert_left(4)

tree.insert_right(10)
tree.insert_right(9)
tree.right_child.insert_left(6)
tree.right_child.insert_left(7)
tree.right_child.left_child.insert_right(8)

inorder(tree)

print()
print("---------------------")

tree.width_invert()

inorder(tree)

print()
print("---------------------")

deep_invert(tree)

inorder(tree)

print()
print("---------------------")

for i in range(1, 11):
    if tree.has_leaf_node(i):
        print(i)

