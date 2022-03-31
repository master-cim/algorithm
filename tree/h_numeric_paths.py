# H. Числовые пути
# 66615019

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def tree_paths_sum(root, val):
    if root is None:
        return 0
    val = (val*10 + root.value)
    if root.left is None and root.right is None:
        return val
    return (tree_paths_sum(root.left, val) +
            tree_paths_sum(root.right, val))


def solution(root):
    return tree_paths_sum(root, 0)


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275