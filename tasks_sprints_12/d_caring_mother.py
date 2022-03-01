# D. Заботливая мама
# ID успешной посылки 65663041

class Node:  
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, elem):
    count = 0
    while node.value != elem:
        if node.value != elem and node.next_item is None:
            count = -1
            break
        else:
            count = count + 1
            node = node.next_item
    return count


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0, "node4")
    # result is idx == 2


if __name__ == '__main__':
    test()
