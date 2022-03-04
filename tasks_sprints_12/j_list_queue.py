# J. Списочная очередь
# ID успешной посылки 65734880

from typing import List, Tuple


class ListQueue:
    def __init__(self):
        self._items = []
        self.top = -1

    def put(self, item: int):
        self.top += 1
        self._items.append(int(item))

    def get(self):
        try:
            if self.isEmpty():
                return('error')
            else:
                self.top -= 1
                return self._items.pop(0)
        except IndexError:
            return('error')

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def size(self):
        return len(self._items)


def run_stack(quantum_command: int,
              command_list: List[List[str]]):
    stack = ListQueue()
    for command in range(0, quantum_command):
        if command_list[command][0] == 'put':
            stack.put(command_list[command][1])
        elif command_list[command][0] == 'get':
            pop_value = stack.get()
            print(pop_value)
        elif command_list[command][0] == 'size':
            len_queue = stack.size()
            print(len_queue)


def read_input() -> Tuple[List[List[str]]]:
    quantum_command = int(input())
    command_list = []
    for _ in range(quantum_command):
        command_list.append(list(map(str, input().strip().split())))
    return(quantum_command, command_list)


if __name__ == '__main__':
    quantum_command, command_list = read_input()
    run_stack(quantum_command, command_list)
