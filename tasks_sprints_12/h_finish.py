# H. Скобочная последовательность
# ID успешной посылки 65708963


def is_correct_bracket_seq(bracket_list):
    while '()' in bracket_list or '[]' in bracket_list or '{}' in bracket_list:
        bracket_list = bracket_list.replace('()', '')
        bracket_list = bracket_list.replace('[]', '')
        bracket_list = bracket_list.replace('{}', '')
    return not bracket_list


def read_input():
    bracket_list = input()
    return(bracket_list)


if __name__ == '__main__':
    command_list = read_input()
    print(is_correct_bracket_seq(command_list))
