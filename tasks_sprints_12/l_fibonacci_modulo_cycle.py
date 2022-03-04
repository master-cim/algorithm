# L. Фибоначчи по модулю
# ID успешной посылки 65746418


def code_amount(k: int, n_intern: int):
    if n_intern == 1 or n_intern == 0:
        return 1
    previous, c_amount = 0, 1
    degrees = 10 ** k
    for _ in range(1, n_intern + 1):
        previous, c_amount = c_amount, previous + c_amount
        c_amount %= degrees
    return c_amount


def read_input():
    n_k_nambers = [int(element) for element in input().strip().split()]
    n_intern = n_k_nambers[0]
    k = n_k_nambers[1]
    return(k, n_intern)


if __name__ == '__main__':
    k, n_intern = read_input()
    print(code_amount(k, n_intern))
