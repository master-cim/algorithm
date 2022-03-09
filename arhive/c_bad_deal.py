# C. Нелюбимое дело
# ID успешной посылки 


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def print_linked_list(node):
    while node:
        if node.next_item is not None:
            print(node.value, end=" -> ")
        else:
            print(node.value)
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
        print_linked_list(new_head)
    else:
        previous_node = get_node_by_index(node, idx-1)
        del_node = get_node_by_index(node, idx)
        previous_node.next_item = del_node.next_item
        print_linked_list(node)


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0, 0)


if __name__ == '__main__':
    test()
