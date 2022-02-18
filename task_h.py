from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    # right = max(len(first_number), len(second_number))
    # print(right)
    result = []
    bufer = '0'
    for i in range(0, max(len(first_number), len(second_number))):
        if first_number[-i] != second_number[-i] and bufer == '0':
            result.append('1')
        elif first_number[-i] != second_number[-i] and bufer == '1':
            result.append('0')
            bufer = '1'
        elif first_number[-i] == '0' and second_number[-i] == '0' and bufer == '0':
            result.append('0')
        elif first_number[-i] == '0' and second_number[-i] == '0' and bufer == '1':
            result.append('1')
        elif first_number[-i] == '1' and second_number[-i] == '1' and bufer == '0':
            result.append('0')
            bufer = '1'
        elif first_number[-i] == '1' and second_number[-i] == '1' and bufer == '1':
            result.append('1')
            bufer = '1'
        print(f'F {first_number[-i]} S {second_number[-i]} B {bufer}')
    return result


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))