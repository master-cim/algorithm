# Задача A. Дек
# ID успешной посылки

from typing import List, Tuple


class DequeCircularBuffer:
    def __init__(self, size):
        self.arr = [0] * size
        self.front = -1
        self.back = 0
        self.size = size

    def push_front(self, value):
        if (self.isFull()):
            print("error")
        if (self.front == -1):
            self.front = 0
            self.back = 0
        elif (self.front == 0):
            self.front = self.size - 1
        else:
            self.front = self.front - 1
        self.arr[self.front] = value
        print(self.arr)

    def push_back(self, value):
        if (self.isFull()):
            print('error')
        if (self.front == -1):
            self.front = 0
            self.back = 0
        elif (self.back == self.size-1):
            self.back = 0
        else:
            self.back = self.back + 1
        self.arr[self.back] = value
        print(self.arr)

    def pop_front(self):
        if (self.isEmpty()):
            print('error')
        if (self.front == self.back):
            print(self.arr[self.front])
            self.front = -1
            self.back = -1
        else:
            if (self.front == self.size - 1):
                print(self.arr[self.front])
                self.front = 0
            else:
                self.front = self.front + 1

    def pop_back(self):
        if (self.isEmpty()):
            print('error')
        if (self.front == self.back):
            print(self.arr[self.back])
            self.front = -1
            self.back = -1
        elif (self.back == 0):
            print(self.arr[self.back])
            self.back = self.size-1
        else:
            print(self.arr[self.back])
            self.back = self.back-1

    def isFull(self):
        return ((self.front == 0 and self.back == self.size-1)
                or self.front == self.back + 1)

    def isEmpty(self):
        return (self.front == -1)


def run_effective_deque(number_command: int,
                        max_len_deque: int, command_list: List[List[str]]):
    deque = DequeCircularBuffer(max_len_deque)
    for command in range(0, number_command):
        if command_list[command][0] == 'push_front':
            deque.push_front(command_list[command][1])
        elif command_list[command][0] == 'push_back':
            deque.push_back(command_list[command][1])
        elif command_list[command][0] == 'pop_front':
            deque.pop_front()
        elif command_list[command][0] == 'pop_back':
            deque.pop_back()


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
