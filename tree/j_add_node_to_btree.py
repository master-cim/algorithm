# J. Добавь узел


class Node:  
    def __init__(self, left=None, right=None, value=0):
        self.right = right
        self.left = left
        self.value = value


def insert(root, key):
    newnode = Node(key)
    pointer_to_start = root
    pointer_to_trailing = None
    while (pointer_to_start is not None):
        pointer_to_trailing = pointer_to_start
        if (key < pointer_to_start.value):
            pointer_to_start = pointer_to_start.left
        else:
            pointer_to_start = pointer_to_start.right
    if (pointer_to_trailing is None):
        pointer_to_trailing = newnode
    elif (key < pointer_to_trailing.value):
        pointer_to_trailing.left = newnode
    else:
        pointer_to_trailing.right = newnode
    return pointer_to_trailing


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6