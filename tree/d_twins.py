# D. Деревья - близнецы.
# ID успешной посылки 66603283


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root1, root2):
    if root1 is None and root2 is None:
        return True
    if (root1 is not None and root2 is not None):
        if root1.value == root2.value:
            return (solution(root1.left, root2.left)
                    and solution(root1.right, root2.right))
    return False


def test():
    node1 = Node(1,  None,  None)
    node2 = Node(2,  None,  None)
    node3 = Node(3,  node1,  node2)

    node4 = Node(1, None,  None)
    node5 = Node(2, None, None)
    node6 = Node(3, node4, node5)
    
    assert solution(node3, node6)
