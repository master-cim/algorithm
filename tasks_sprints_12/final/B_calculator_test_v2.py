# B. Калькулятор
# ID успешной посылки
from typing import Tuple
import operator


def calculator(put_items: Tuple[str]):
    stack_items = []
    list_operations = ('-', '+', '*', '/')
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
        }
    for step in range(0, len(put_items)):
        if put_items[step] not in list_operations:
            stack_items.append(put_items[step])
        else:
            op_char = stack_items[step]
            x = stack_items.pop(-2)
            y = stack_items.pop(-1)
            expr = ops[op_char]
            result = expr(x, y)
            stack_items.append(result)
    print(int(stack_items[-1]))


def read_input() -> Tuple[str]:
    put_items = tuple(map(str, input().strip().split()))
    return put_items


if __name__ == '__main__':
    put_items = read_input()
    calculator(put_items)
