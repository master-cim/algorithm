# B. Калькулятор
# ID успешной посылки 65886740
from typing import Tuple
import operator

OPERATORS = {
    '-': operator.sub,
    '+': operator.add,
    '*': operator.mul,
    '/': operator.floordiv
}


def calculator(put_items: Tuple[str]):
    stack_items = []
    list_operations = ('-', '+', '*', '/')
    for step in range(0, len(put_items)):
        if put_items[step] not in list_operations:
            stack_items.append(put_items[step])
        else:
            x = stack_items.pop(-2)
            y = stack_items.pop(-1)
            operator = OPERATORS[put_items[step]]
            stack_items.append(operator(float(x), float(y)))
    return(int(stack_items[-1]))


def read_input() -> Tuple[str]:
    put_items = tuple(map(str, input().strip().split()))
    return put_items


if __name__ == '__main__':
    put_items = read_input()
    print(calculator(put_items))
