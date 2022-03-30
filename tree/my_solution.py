# C. Дерево - анаграмма


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root):
    if root is None:
        return True
    if (root.left is None and root.right is None):
        return True
    if (root.left is None or root.right is None):
        return False
    queue_left = []
    queue_right = []
    queue_left.append(root.left)
    queue_right.append(root.right)
    while 1:
        q_size_lft = len(queue_left)
        q_size_rght = len(queue_right)
        if q_size_lft != q_size_rght:
            return False
        if q_size_lft == 0:
            break
    curr_lvl_left = []
    curr_lvl_rght = []
    while q_size_lft > 0:
        node_lft = queue_left[0]
        queue_left.pop(0)
        if node_lft.left is not None:
            queue_left.append(node_lft.left)
        if node_lft.right is not None:
            queue_left.append(node_lft.right)
        node_lft -= 1
        node_rght = queue_right[0]
        queue_right.pop(0)
        if node_rght.left is not None:
            queue_right.append(node_rght.left)
        if node_rght.right is not None:
            queue_right.append(node_rght.right)
        curr_lvl_left.sort()
        curr_lvl_rght.sort()
        if curr_lvl_left != curr_lvl_rght:
            return False
        return True


def test():
    node1 = Node(3,  None,  None)
    node2 = Node(4,  None,  None)
    node3 = Node(4,  None,  None)
    node4 = Node(3,  None,  None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)
