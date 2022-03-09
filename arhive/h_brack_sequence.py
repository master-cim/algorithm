# H. Скобочная последовательность
# ID успешной посылки
# не проходит вариант (){}[] и ({})({[]}[])
from typing import List, Tuple


def is_correct_bracket_seq(bracket_list):
    members = len(bracket_list)
    if bracket_list == []:
        return True
    if members % 2 != 0:
        return False
    midle = int(members / 2)
    idx_forward = 0
    idx_back = -1
    count = 0
    while (idx_forward < midle) and (
        (bracket_list[idx_forward] + bracket_list[idx_back]) == '[]'
        or (bracket_list[idx_forward] + bracket_list[idx_back]) == '{}'
        or (bracket_list[idx_forward] + bracket_list[idx_back]) == '()'
    ):
        idx_forward += 1
        idx_back -= 1
        count += 1
    if count == midle:
        return True
    else:
        return False


def read_input() -> Tuple[List[List[str]]]:
    bracket_list = list(input())
    return(bracket_list)


if __name__ == '__main__':
    command_list = read_input()
    print(is_correct_bracket_seq(command_list))
