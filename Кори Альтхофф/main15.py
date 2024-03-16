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


def inorder(a_tree):
    if a_tree:
        inorder(a_tree.left_child)
        print(a_tree.key, end=" ")
        inorder(a_tree.right_child)


def if_min_heap(a_tree):
    if a_tree:
        if a_tree.right_child is not None:
            if a_tree.right_child.key < a_tree.key:
                return False
            if_min_heap(a_tree.right_child)
        if a_tree.left_child is not None:
            if a_tree.left_child.key < a_tree.key:
                return False
            if_min_heap(a_tree.left_child)
    return True


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

print(if_min_heap(tree))

print("---------------------")

tree2 = BinaryTree(1)
tree2.insert_left(6)
tree2.insert_left(4)
tree2.left_child.insert_right(5)
tree2.insert_left(3)

tree2.insert_right(8)
tree2.insert_right(2)
tree2.right_child.insert_left(10)
tree2.right_child.insert_left(7)
tree2.right_child.left_child.insert_right(9)

inorder(tree2)

print()
print("---------------------")

print(if_min_heap(tree2))
