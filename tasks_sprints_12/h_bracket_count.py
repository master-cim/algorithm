# H. Скобочная последовательность
# ID успешной посылки
# не проходит вариант )( и ([)]
from typing import List, Tuple
from collections import Counter


def is_correct_bracket_seq(bracket_list):
    if bracket_list == []:
        return True
    col_br = Counter(bracket_list)
    if (col_br['['] == col_br[']']
        and col_br['{'] == col_br['}']
        and col_br['('] == col_br[')']):
        return True
    else:
        return False


def read_input() -> Tuple[List[List[str]]]:
    bracket_list = list(input())
    return(bracket_list)


if __name__ == '__main__':
    command_list = read_input()
    print(is_correct_bracket_seq(command_list))
