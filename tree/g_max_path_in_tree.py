# G. Максимальный путь в дереве
# 66613611


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def fin_max_sum(root) -> int:
    if root is None:
        return 0
    lft = fin_max_sum(root.left)
    rght = fin_max_sum(root.right)
    max_single = max(max(lft, rght) + root.value, root.value)
    max_top = max(max_single, lft + rght + root.value)
    fin_max_sum.res = max(fin_max_sum.res, max_top)
    return max_single


def solution(root):
    fin_max_sum.res = float("-inf")
    fin_max_sum(root)
    return fin_max_sum.res


def test():
    node1 = Node(5, None, None)
    node2 = Node(1, None, None)
    node3 = Node(-3, node2, node1)
    node4 = Node(2, None, None)
    node5 = Node(2, node4, node3)
    assert solution(node5) == 6