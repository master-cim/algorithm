# C. Дерево - анаграмма


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def deep(root) -> int:
    if root is None:
        return 0
    return max(deep(root)) + 1


def solution(root):
    if root is None:
        return False
    if (root.left is None and root.right is None):
        return True
    if (root.left is None or root.right is None):
        return False
    if (root.left is not None and root.right is not None):
        if root.left.value == root.right.value:
            return (solution(root.left)
                    and solution(root.right))
    if deep(root.left) == deep(root.right):
        return True
    return False


def test():
    node1 = Node(3,  None,  None)
    node2 = Node(4,  None,  None)
    node3 = Node(4,  None,  None)
    node4 = Node(3,  None,  None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)
