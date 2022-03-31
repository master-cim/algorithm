# J. Добавь узел


class Node:  
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def insert(root, key):
    if not root:
        root = Node(key)
        return
    q = []
    q.append(root)
    while (len(q)):
        root = q[0]
        q.pop(0)
        if (not root.left):
            root.left = Node(key)
            break
        else:
            q.append(root.left)
        if (not root.right):
            root.right = Node(key)
            break
        else:
            q.append(root.right)


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6