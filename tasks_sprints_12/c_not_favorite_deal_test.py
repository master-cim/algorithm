# C. Нелюбимое дело
# ID успешной посылки 65659820


class Node:
    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item


def print_linked_list(node):
    while node:
        print(node.value, end="\n")
        node = node.next_item


def get_node_by_index(node, index):
    while index:
        node = node.next_item
        index -= 1
    return node


def solution(node, idx):
    if idx == 0:
        idx += 1
        new_head = node.next_item
        return new_head
    else:
        previous_node = get_node_by_index(node, idx-1)
        del_node = get_node_by_index(node, idx)
        previous_node.next_item = del_node.next_item
        return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0, 2)


if __name__ == '__main__':
    test()
