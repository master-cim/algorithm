# L. Два велосипеда
# ID успешной посылки не проходит по времени


def amount_for_bike(cash_per_day, cost_bike):
    result = next((cash_per_day.index(x)+1 for x in cash_per_day if x >= cost_bike), '-1')
    return result


def read_input():
    _ = int(input())
    cash_per_day = [int(element) for element in input().strip().split()]
    cost_bike = int(input())
    return(cash_per_day, cost_bike)


if __name__ == '__main__':
    cash_per_day, cost_bike = read_input()
    print( amount_for_bike(cash_per_day, cost_bike),  amount_for_bike(cash_per_day, cost_bike*2))
