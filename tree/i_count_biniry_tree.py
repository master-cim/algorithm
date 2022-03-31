# I. Разные деревья поиска
# 66616805


def binomial_coefficient(n, k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

 
def count_possible_trees(n):
    c = binomial_coefficient(2 * n, n)
    count = c // (n + 1)
    return count


def read_input():
    n = input()
    return(int(n))


if __name__ == '__main__':
    n = read_input()
    print(count_possible_trees(n))
