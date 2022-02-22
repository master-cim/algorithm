from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    first = len(first_number)
    second = len(second_number)
    if first > second:
        second_number = second_number.zfill(first)
    else:
        first_number = first_number.zfill(second)
    f = first_number[::-1]
    s = second_number[::-1]
    result = []
    bufer = '0'
    for i in range(0, max(first, second)):
        if f[i] != s[i] and bufer == '0':
            result.append('1')
        elif f[i] != s[i] and bufer == '1':
            result.append('0')
            bufer = '1'
        elif f[i] == '0' and s[i] == '0' and bufer == '0':
            result.append('0')
            bufer = '0'
        elif f[i] == '0' and s[i] == '0' and bufer == '1':
            result.append('1')
            bufer = '0'
        elif f[i] == '1' and s[i] == '1' and bufer == '0':
            result.append('0')
            bufer = '1'
        elif f[i] == '1' and s[i] == '1' and bufer == '1':
            result.append('1')
            bufer = '1'
    if bufer == '0':
        result = ''.join(result)
        return result[::-1]
    else:
        result.append(bufer)
    result = ''.join(result)
    return result[::-1]


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
