# I. Ограниченная очередь

from typing import List, Tuple


class MyQueueSized:
    def __init__(self, max_size: int):
        self._items = []
        self.top = -1
        self.max = max_size

    def push(self, item: int):
        if self.isFull():
            print('error')
            return
        else:
            self.top += 1
            self._items.append(int(item))

    def pop(self):
        try:
            if self.isEmpty():
                print('None')
                return
            else:
                self.top -= 1
                return self._items.pop()
        except IndexError:
            print('error')

    def peek(self):
        if self.top is None:
            print('None')
        else:
            print(self.top)

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top == self.max - 1:
            return True
        else:
            return False

    def size(self):
        return len(self._items)


def run_stack(quantum_command: int, queue_length: int, command_list: List[List[str]]):
    max_size = queue_length
    stack = MyQueueSized(max_size)
    for command in range(0, quantum_command):
        if command_list[command][0] == 'push':
            stack.push(command_list[command][1])
        elif command_list[command][0] == 'pop':
            stack.pop()
        elif command_list[command][0] == 'peek':
            peek_value = stack.peek()
            print(peek_value)
        elif command_list[command][0] == 'size':
            len_queue = stack.size()
            print(len_queue)


def read_input() -> Tuple[List[List[str]]]:
    quantum_command = int(input())
    queue_length = int(input())
    command_list = []
    for _ in range(quantum_command):
        command_list.append(list(map(str, input().strip().split())))
    print(quantum_command, queue_length, command_list)
    return(quantum_command, queue_length, command_list)


if __name__ == '__main__':
    quantum_command, queue_length, command_list = read_input()
    run_stack(quantum_command, queue_length, command_list)
