# Задача A. Дек
# ID успешной посылки 	65850972
# ID успешной посылки перехват исключения 65930403
# ID успешной посылки c использованием getattr 65930764

from typing import List, Tuple


class Error(Exception):
    pass


class DequeIsFullError(Error):
    pass


class DequeIsEmptyError(Error):
    pass


class DequeCircularBuffer:
    def __init__(self, size):
        self.__queue = [None] * size
        self.__f_head = 0
        self.__f_tail = 0
        self.__b_head = size - 1
        self.__b_tail = size - 1
        self.__max_n = size
        self.__size = 0

    def push_front(self, value):
        if self.__size != self.__max_n:
            self.__queue[self.__f_tail] = value
            self.__f_tail = (self.__f_tail + 1) % self.__max_n
            self.__size += 1
        else:
            raise DequeIsFullError

    def push_back(self, value):
        if self.__size != self.__max_n:
            self.__queue[self.__b_tail] = value
            self.__b_tail = (self.__b_tail - 1) % self.__max_n
            self.__size += 1
        else:
            raise DequeIsFullError

    def pop_front(self):
        if self._is_empty():
            raise DequeIsEmptyError
        if self.__queue[self.__f_head] is None:
            value = self.__queue[self.__b_head]
            self.__queue[self.__b_head] = None
            self.__b_head = (self.__b_head - 1) % self.__max_n
            self.__f_head = (self.__f_head - 1) % self.__max_n
            self.__f_tail = (self.__f_tail - 1) % self.__max_n
            self.__size -= 1
        else:
            value = self.__queue[self.__f_tail-1]
            self.__queue[self.__f_tail-1] = None
            self.__f_tail = (self.__f_tail - 1) % self.__max_n
            self.__size -= 1
        return value

    def pop_back(self):
        if self._is_empty():
            raise DequeIsEmptyError
        if self._is_full():
            value = self.__queue[(self.__b_tail + 1) % self.__max_n]
            self.__queue[(self.__b_tail + 1) % self.__max_n] = None
            self.__b_tail = (self.__b_tail + 1) % self.__max_n
            self.__size -= 1
        elif self.__queue[self.__b_head] is None:
            value = self.__queue[self.__f_head]
            self.__queue[self.__f_head] = None
            self.__f_head = (self.__f_head + 1) % self.__max_n
            self.__b_head = (self.__b_head + 1) % self.__max_n
            self.__b_tail = (self.__b_tail + 1) % self.__max_n
            self.__size -= 1
        else:
            value = self.__queue[(self.__b_tail + 1) % self.__max_n]
            self.__queue[(self.__b_tail + 1) % self.__max_n] = None
            self.__b_tail = (self.__b_tail + 1) % self.__max_n
            self.__size -= 1
        return value

    def _is_full(self):
        return self.__size == self.__max_n

    def _is_empty(self):
        return self.__size == 0


def run_effective_deque(number_command: int,
                        max_len_deque: int, command_list: List[List[str]]):
    deque = DequeCircularBuffer(max_len_deque)
    for command in range(0, number_command):
        try:
            if (command_list[command][0] == 'push_front'
               or command_list[command][0] == 'push_back'):
                result = getattr(deque, command_list[command][0])
                result((command_list[command][1]))
            else:
                result = getattr(deque, command_list[command][0])
                print(result())
        except DequeIsFullError:
            print('error')
        except DequeIsEmptyError:
            print('error')


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
