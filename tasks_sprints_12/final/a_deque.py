# Задача A. Дек
# ID успешной посылки

from typing import List, Tuple


class DequeCircularBuffer:
    def __init__(self, size):
        self.arr = [0] * size
        self.start = -1
        self.end = 0
        self.size = size

    # добавить элемент в начало дека. 
    # Если в деке уже находится максимальное число элементов, вывести «error».
    def push_front(self, value):
        # проверка на заполненность Дека
        if (self.isFull()):
            print("Переполнено")
            return
        # Проверка на то что очередь в начале пуста
        if (self.start == -1):
            self.start = 0
            self.end = 0
        # старт находиться в первой позиции очереди
        elif (self.start == 0):
            self.start = self.size - 1
        else: # уменьшить конец части старт на единицу
            self.start = self.start-1
        # вставить текущий элемент в Deque
        self.arr[self.start] = value

    # добавить элемент в конец дека. 
    # Если в деке уже находится максимальное число элементов, вывести «error».
    def push_back(self, value):
        if (self.isFull()):
            print(" Overflow")
            return
        # Если очередь изначально пуста
        if (self.front == -1):
            self.front = 0
            self.rear = 0

        # END находится в последней позиции очереди
        elif (self.rear == self.size-1):
            self.rear = 0

        # увеличить  конец END на '1'
        else:
            self.rear = self.rear+1

        # вставить текущий элемент в Deque
        self.arr[self.rear] = value

    # вывести первый элемент дека и удалить его.
    # Если дек был пуст, то вывести «error».
    def pop_front(self):
        # проверить, пуста ли Deque или нет
        if (self.isEmpty()):
            print("Queue Underflow")
            return
        # Deque имеет только один элемент
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            # вернуться в исходное положение
            if (self.front == self.size - 1):
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
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        elif (self.rear == 0):
            self.rear = self.size-1
        else:
            self.rear = self.rear-1
      
    # Возвращает передний элемент Deque
    def getFront(self):
        # проверить, пуста ли Deque или нет
        if (self.isEmpty()):
            print(" Underflow")
            return -1
          
        return self.arr[self.front]
      
      
    # функция возвращает задний элемент Deque
    def getRear(self):
        # проверить, пуста ли Deque или нет
        if(self.isEmpty() or self.rear < 0):
            print(" Underflow");
            return -1 ;
          
        return self.arr[self.rear];
    # def push(self, item: int):
    #     self._items.append(int(item))
    #     if (len(self._items) == 1):
    #         self.trackDeque.append(int(item))
    #         return
    #     if (int(item) > self.trackDeque[-1]):
    #         self.trackDeque.append(int(item))
    #     else:
    #         self.trackDeque.append(self.trackDeque[-1])

    # def pop(self):
    #     try:
    #         self._items.pop()
    #         self.trackDeque.pop()
    #     except IndexError:
    #         print('error')

    # def get_max(self):
    #     if self.trackDeque != []:
    #         return self.trackDeque[-1]
    #     else:
    #         return('None')

    # Проверяем заполнен Deque или нет.
    def isFull(self):
        return ((self.start == 0 and self.end == self.size-1)
                or self.start == self.end + 1)

    # Проверяем пустой Deque или нет.
    def isEmpty(self):
        return (self.front == -1)


def run_effective_deque(number_command: int,
              max_len_deque: int, command_list: List[List[str]]):
    max_size = max_len_deque
    deque =  DequeCircularBuffer(max_size)
    for command in range(0, number_command):
        if command_list[command][0] == 'push':
            deque.push(command_list[command][1])
        elif command_list[command][0] == 'pop':
            pop_value = deque.pop()
            print(pop_value)
        elif command_list[command][0] == 'peek':
            peek_value = deque.peek()
            print(peek_value)
        elif command_list[command][0] == 'size':
            len_queue = deque.size()
            print(len_queue)


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