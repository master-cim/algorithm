# Задача A. Дек
# ID успешной посылки

from typing import List, Tuple


class DequeCircularBuffer:
    def __init__(self, size):
        self.arr = [0] * size
        self.front = -1
        self.back = 0
        self.size = size

    # добавить элемент в начало дека.
    # Если в деке уже находится максимальное число элементов, вывести «error».
    def push_front(self, value):
        # проверка на заполненность Дека
        if (self.isFull()):
            print("error")
            return
        # Проверка на то что очередь в начале пуста
        if (self.front == -1):
            self.front = 0
            self.back = 0
        # старт находиться в первой позиции очереди
        elif (self.front == 0):
            self.front = self.size - 1
        else: # уменьшить конец части старт на единицу
            self.front = self.front-1
        # вставить текущий элемент в Deque
        self.arr[self.front] = value


    # добавить элемент в конец дека. 
    # Если в деке уже находится максимальное число элементов, вывести «error».
    def push_back(self, value):
        if (self.isFull()):
            print("error")
            return
        # Если очередь изначально пуста
        if (self.front == -1):
            self.front = 0
            self.back = 0

        # END находится в последней позиции очереди
        elif (self.back == self.size-1):
            self.back = 0

        # увеличить  конец END на '1'
        else:
            self.back = self.back+1

        # вставить текущий элемент в Deque
        self.arr[self.back] = value


    # вывести первый элемент дека и удалить его.
    # Если дек был пуст, то вывести «error».
    def pop_front(self):
        # проверить, пуста ли Deque или нет
        if (self.isEmpty()):
            print("Queue Underflow")
            return
        # Deque имеет только один элемент
        if (self.front == self.back):
            print(self.arr[self.front])
            self.front = -1
            self.back = -1
        else:
            # вернуться в исходное положение
            if (self.front == self.size - 1):
                print(self.arr[self.front])
                self.front = 0
            else: # увеличьте фронт на «1», чтобы удалить текущее значение фронта из Deque
                self.front = self.front + 1

    # вывести последний элемент дека и удалить его.
    # Если дек был пуст, то вывести «error».
    def pop_back(self):
        if (self.isEmpty()):
            print(" Underflow")
            return
        # Deque имеет только один элемент
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
      
    # Возвращает передний элемент Deque
    def getFront(self):
        # проверить, пуста ли Deque или нет
        if (self.isEmpty()):
            print(" Underflow")
            return -1
        return self.arr[self.front]

    # функция возвращает задний элемент Deque
    def getBack(self):
        # проверить, пуста ли Deque или нет
        if(self.isEmpty() or self.back < 0):
            print(" Underflow")
            return -1
        return self.arr[self.back]

    # Проверяем заполнен Deque или нет.
    def isFull(self):
        return ((self.front == 0 and self.back == self.size-1)
                or self.front == self.back + 1)

    # Проверяем пустой Deque или нет.
    def isEmpty(self):
        return (self.front == -1)


def run_effective_deque(number_command: int,
                        max_len_deque: int, command_list: List[List[str]]):
    max_size = max_len_deque
    deque = DequeCircularBuffer(max_size)
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