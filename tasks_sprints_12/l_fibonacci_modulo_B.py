# L. Фибоначчи по модулю
# ID успешной посылки

def code_amount(k: int, n_intern: int):
    if n_intern == 1 or n_intern == 0:
        return 1
    root_5 = 5 ** 0.5
    phi = ((1 + root_5) / 2)
    c_amount = ((phi ** n_intern) - ((-phi) ** -n_intern)) / root_5
    result = c_amount % 10 ** k
    print(c_amount)
    return round(result)


def read_input():
    n_k_nambers = [int(element) for element in input().strip().split()]
    n_intern = n_k_nambers[0]
    k = n_k_nambers[1]
    return(k, n_intern)


if __name__ == '__main__':
    k, n_intern = read_input()
    print(code_amount(k, n_intern))
