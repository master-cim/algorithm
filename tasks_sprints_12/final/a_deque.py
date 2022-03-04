# Задача A. Дек
# ID успешной посылки

from typing import List, Tuple


class DequeCircularBuffer:
    def __init__(self):
        self._items = []
        self.trackStack = []

    def push(self, item: int):
        self._items.append(int(item))
        if (len(self._items) == 1):
            self.trackStack.append(int(item))
            return
        if (int(item) > self.trackStack[-1]):
            self.trackStack.append(int(item))
        else:
            self.trackStack.append(self.trackStack[-1])

    def pop(self):
        try:
            self._items.pop()
            self.trackStack.pop()
        except IndexError:
            print('error')

    def get_max(self):
        if self.trackStack != []:
            return self.trackStack[-1]
        else:
            return('None')

def run_effective_deque()


def read_input() -> Tuple[List[List[str]]]:
    number_command = int(input())
    max_len_deque = int(input())
    command_list = []
    for _ in range(number_command):
        command_list.append(list(map(str, input().strip().split())))
    return(number_command, max_len_deque, command_list)


if __name__ == '__main__':
    number_command, max_len_deque, command_list = read_input()
    run_effective_deque(number_command, max_len_deque, command_list)


# def test():
#     node3 = Node("node3", None)
#     node2 = Node("node2", node3)
#     node1 = Node("node1", node2)
#     node0 = Node("node0", node1)
#     solution(node0)
#     # Output is:
#     # node0
#     # node1
#     # node2
#     # node3


# if __name__ == '__main__':
#     test()