# K. Рекурсивные числа Фибоначчи
# ID успешной посылки 65735941


def code_amount(n_intern: int):
    if n_intern == 1 or n_intern == 0:
        return 1
    return code_amount(n_intern - 1) + code_amount(n_intern - 2)


def read_input() -> int:
    n_intern = int(input())
    return(n_intern)


if __name__ == '__main__':
    n_intern = read_input()
    print(code_amount(n_intern))
