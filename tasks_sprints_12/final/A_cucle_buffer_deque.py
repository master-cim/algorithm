# Задача A. Дек
# ID успешной посылки 	65850972

from typing import List, Tuple


class DequeCircularBuffer:
    def __init__(self, size):
        self.queue = [None] * size
        self.f_head = 0
        self.f_tail = 0
        self.b_head = size - 1
        self.b_tail = size - 1
        self.max_n = size
        self.size = 0

    def push_front(self, value):
        if self.isFull():
            print('error')
        if self.size != self.max_n:
            self.queue[self.f_tail] = value
            self.f_tail = (self.f_tail + 1) % self.max_n
            self.size += 1

    def push_back(self, value):
        if self.isFull():
            print('error')
        if self.size != self.max_n:
            self.queue[self.b_tail] = value
            self.b_tail = (self.b_tail - 1) % self.max_n
            self.size += 1

    def pop_front(self):
        if self.isEmpty():
            return 'error'
        if self.queue[self.f_head] is None:
            value = self.queue[self.b_head]
            self.queue[self.b_head] = None
            self.b_head = (self.b_head - 1) % self.max_n
            self.f_head = (self.f_head - 1) % self.max_n
            self.f_tail = (self.f_tail - 1) % self.max_n
            self.size -= 1
        else:
            value = self.queue[self.f_tail-1]
            self.queue[self.f_tail-1] = None
            self.f_tail = (self.f_tail - 1) % self.max_n
            self.size -= 1
        return value

    def pop_back(self):
        if self.isEmpty():
            return 'error'
        if self.isFull():
            value = self.queue[(self.b_tail + 1) % self.max_n]
            self.queue[(self.b_tail + 1) % self.max_n] = None
            self.b_tail = (self.b_tail + 1) % self.max_n
            self.size -= 1
        elif self.queue[self.b_head] is None:
            value = self.queue[self.f_head]
            self.queue[self.f_head] = None
            self.f_head = (self.f_head + 1) % self.max_n
            self.b_head = (self.b_head + 1) % self.max_n
            self.b_tail = (self.b_tail + 1) % self.max_n
            self.size -= 1
        else:
            value = self.queue[(self.b_tail + 1) % self.max_n]
            self.queue[(self.b_tail + 1) % self.max_n] = None
            self.b_tail = (self.b_tail + 1) % self.max_n
            self.size -= 1
        return value

    def isFull(self):
        return self.size == self.max_n

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
