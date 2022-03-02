# F. Стек - Max
# ID успешной посылки 65680227

from typing import List, Tuple


class StackMax:
    def __init__(self):
        self._items = []

    def push(self, item: int):
        self._items.append(int(item))

    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            print('error')

    def get_max(self):
        if self._items != []:
            return max(self._items)
        else:
            return('None')

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f'{self._items}'


def run_stack(command_list: List[List[str]]):
    stack = StackMax()
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
