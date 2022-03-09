# B. Калькулятор
# ID успешной посылки

from typing import Tuple


def calculator(put_items: Tuple[str]):
    stack_items = []
    # top = -1
    list_operations = ('-', '+', '*', '/')
    for step in range(0, len(put_items)):
        if put_items[step] not in list_operations:
            stack_items.append(put_items[step])
        else:
            x = int(stack_items[step-2]) * int(stack_items[step-1])
            stack_items.append(str(x))
            print(x)
        print(stack_items)



def read_input() -> Tuple[str]:
    put_items = tuple(map(str, input().strip().split()))
    return put_items


if __name__ == '__main__':
    put_items = read_input()
    calculator(put_items)
