# B. Калькулятор
# ID успешной посылки
from __future__ import division
from typing import Tuple
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


# class MyCalculate:
#     def __init__(self, val_x, val_y):
#         self.value_x = val_x
#         self.value_y = val_y

#     def multiplication(self, value_x, value_y):
#         return int(value_x) * int(value_y)

#     def devision(self, value_x, value_y):
#         result = float(value_x) / float(value_y)
#         if result <= 0:
#             return round(result)
#         return result

#     def subtraction(self, value_x, value_y):
#         return (value_x) - (value_y)

#     def addition(self, value_x, value_y):
#         return int(value_x) + int(value_y)


def calculator(put_items: Tuple[str]):
    stack_items = []
    stack_opr = []
    list_operations = ('-', '+', '*', '/')
    for step in range(0, len(put_items)):
        if put_items[step] not in list_operations:
            stack_items.append(float(put_items[step]))
            print(f'Стек чисел {stack_items}')
        else:
            stack_opr.append(put_items[step])
            print(f'Стек операторов{stack_opr}')
            x = stack_items.pop(-2)
            y = stack_items.pop(-1)
            o = stack_opr.pop()
            print(f'Выражение {x} {o} {y}')
            expr = MyCalculate(x, y)
            dic_match_fn_to_opr = {'-': expr.subtraction(x, y),
                                   '+': expr.addition(x, y),
                                   '*': expr.multiplication(x, y),
                                   '/': expr.devision(x, y)}
            stack_items.append(dic_match_fn_to_opr.get(o))
        print(f'Промежуточный результат {int(stack_items[-1])}')


def read_input() -> Tuple[str]:
    put_items = tuple(map(str, input().strip().split()))
    return put_items


if __name__ == '__main__':
    put_items = read_input()
    calculator(put_items)
