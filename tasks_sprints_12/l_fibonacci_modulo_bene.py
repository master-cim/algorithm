# L. Фибоначчи по модулю
# ID успешной посылки
import decimal


def code_amount(k: int, n_intern: int):
    decimal.getcontext().prec = 10000
    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)
    c_amount = ((phi ** n_intern) - ((-phi) ** -n_intern)) / root_5
    result = round(c_amount) % 10 ** k
    return result


def read_input():
    n_k_nambers = [int(element) for element in input().strip().split()]
    n_intern = n_k_nambers[0] + 1
    k = n_k_nambers[1]
    return(k, n_intern)


if __name__ == '__main__':
    k, n_intern = read_input()
    print(code_amount(k, n_intern))
