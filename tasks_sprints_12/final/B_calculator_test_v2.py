# B. Калькулятор
# ID успешной посылки "список" 65886740
# ID успешной посылки "класс Стек"  65920846
from typing import Tuple
import operator

OPERATORS = {
    '-': 'sub',
    '+': 'add',
    '*': 'mul',
    '/': 'floordiv'
}


class StackOperands:
    def __init__(self):
        self.__items = []

    def push(self, item: int):
        self.__items.append(item)

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            print('error')


def calculator(put_items: Tuple[str]):
    stack_items = StackOperands()
    for step in range(0, len(put_items)):
        if put_items[step] in OPERATORS:
            method = getattr(operator, OPERATORS.get(put_items[step]))
            first_operand = stack_items.pop()
            second_operand = stack_items.pop()
            stack_items.push(method(first_operand, second_operand))
        else:
            stack_items.push(int(put_items[step]))
    return stack_items.pop()


def read_input() -> Tuple[str]:
    put_items = tuple(map(str, input().strip().split()))
    return put_items


if __name__ == '__main__':
    put_items = read_input()
    print(calculator(put_items))
