# A. Лампочки
# ID успешной посылки 66592486

class new_node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def find_max_bulb(root):
    if root is None:
        return float('-inf')
    res = root.data
    left_res = find_max_bulb(root.left)
    right_res = find_max_bulb(root.right)
    if (left_res > res):
        res = left_res
    if (right_res > res):
        res = right_res
    return res

def find_min_bubl(root):
    if root is None:
        return float('inf')
    res = root.data
    lres = find_min_bubl(root.left)
    rres = find_min_bubl(root.right)
    if lres < res:
        res = lres
    if rres < res:
        res = rres
    return res


if __name__ == '__main__':
    root = new_node(1)
    root.left = new_node(3)
    root.right = new_node(5)
    root.left.right = new_node(10)
    root.left.right.right = new_node(3)
    root.left.left = new_node(8)
    root.left.left.left = new_node(14)
    root.left.left.right = new_node(15)
    root.right.right = new_node(6)
    root.right.left = new_node(2)
    root.right.right.left = new_node(0)
    root.right.right.right = new_node(None)

    print("Maximum element is", find_max_bulb(root))
