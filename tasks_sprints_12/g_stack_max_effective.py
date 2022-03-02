# G. Стек - MaxEffective
# ID успешной посылки 65682900
from typing import List, Tuple


class StackMaxEffective:
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


def run_stack(command_list: List[List[str]]):
    stack = StackMaxEffective()
    for command in range(0, len(command_list)):
        if command_list[command][0] == 'push':
            stack.push(command_list[command][1])
        elif command_list[command][0] == 'pop':
            stack.pop()
        elif command_list[command][0] == 'get_max':
            max_value = stack.get_max()
            print(max_value)


def read_input() -> Tuple[List[List[str]]]:
    n = int(input())
    command_list = []
    for _ in range(n):
        command_list.append(list(map(str, input().strip().split())))
    return(command_list)


if __name__ == '__main__':
    command_list = read_input()
    run_stack(command_list)
