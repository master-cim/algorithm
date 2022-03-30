# A. Лампочки
# ID успешной посылки 66592486


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    if root is None:
        return float('-inf')
    res = root.value
    left_res = solution(root.left)
    right_res = solution(root.right)
    if (left_res > res):
        res = left_res
    if (right_res > res):
        res = right_res
    return res


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3
