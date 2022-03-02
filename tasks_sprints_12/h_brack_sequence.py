# H. Скобочная последовательность
# ID успешной посылки
from typing import List, Tuple


def is_correct_bracket_seq(bracket_list):
    members = len(bracket_list)
    if bracket_list == []:
        return True
    if members % 2 != 0:
        return False
    midle = int(members / 2)
    while i < midle:
        if bracket_list[i] members
        i += 1


def read_input() -> Tuple[List[List[str]]]:
    bracket_list = list(input())
    return(bracket_list)


if __name__ == '__main__':
    command_list = read_input()
    print(is_correct_bracket_seq(command_list))
