# L. Фибоначчи по модулю
# ID успешной посылки

cache = {0: 0, 1: 1}


def code_amount(n_intern: int):
    if n_intern == 1 or n_intern == 0:
        return 1
    cache[n_intern] = code_amount(n_intern - 1) + code_amount(n_intern - 2)
    return cache[n_intern]


def k_last_number(k: int, c_amount: int):
    result = c_amount % 10 ** k
    return result


def read_input():
    n_k_nambers = [int(element) for element in input().strip().split()]
    n_intern = n_k_nambers[0]
    k = n_k_nambers[1]
    return(k, n_intern)


if __name__ == '__main__':
    k, n_intern = read_input()
    print(k_last_number(k, code_amount(n_intern)))
