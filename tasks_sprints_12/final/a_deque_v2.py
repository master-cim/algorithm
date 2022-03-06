# Задача A. Дек
# ID успешной посылки

from typing import List, Tuple


class DequeCircularBuffer:
    def __init__(self, size):
        self.queue = []
        self.front = 0
        self.back = 0
        self.max_n = size
        self.size = 0

    def push_front(self, value):
        if self.size != self.max_n:
            self.queue.insert(0, value)
            self.back = (self.back + 1) % self.max_n
            self.size += 1
        print(self.queue)
        print(self.back)

    def push_back(self, value):
        if self.size != self.max_n:
            self.queue.append(value)
            self.front = (self.front - 1) % self.max_n
            self.size += 1
        print(self.queue)
        print(self.front)

    def pop_front(self):
        if self.isEmpty():
            return None
        value = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.max_n
        self.size -= 1
        print(self.queue)
        print(self.size)
        return value



    def pop_back(self):
        if self.isEmpty():
            return None
        value = self.queue[self.back]
        self.queue[self.back] = None
        self.back = (self.back - 1) % self.max_n
        self.size -= 1
        # print(self.queue)
        # print(self.size)
        return value

    def isFull(self):
        if ((self.front == 0 and self.back == self.size-1)
                or self.front == self.back + 1):
            print('error')

    def isEmpty(self):
        return self.size == 0


def run_effective_deque(number_command: int,
                        max_len_deque: int, command_list: List[List[str]]):
    deque = DequeCircularBuffer(max_len_deque)
    for command in range(0, number_command):
        if command_list[command][0] == 'push_front':
            deque.push_front(command_list[command][1])
        elif command_list[command][0] == 'push_back':
            deque.push_back(command_list[command][1])
        elif command_list[command][0] == 'pop_front':
            print(deque.pop_front())
        elif command_list[command][0] == 'pop_back':
            print(deque.pop_back())


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
