# L. Два велосипеда
# ID успешной посылки 


def amount_for_bike(cash_per_day, cost_bike, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if cash_per_day[mid] >= cost_bike:
        mid = next(
            (cash_per_day.index(x)+1 for x in cash_per_day if x >= cost_bike),
            '-1')
        return mid
    elif cash_per_day[mid] > cost_bike:
        result = amount_for_bike(cash_per_day, cost_bike, left, mid-1)
        return result
    else:
        result = amount_for_bike(cash_per_day, cost_bike, mid+1, right)
        return result


def read_input():
    number_days = int(input())
    cash_per_day = [int(element) for element in input().strip().split()]
    cost_bike = int(input())
    two_bikes = cost_bike * 2
    return(number_days, cash_per_day, cost_bike, two_bikes)


if __name__ == '__main__':
    number_days, cash_per_day, cost_bike, two_bikes = read_input()
    print(amount_for_bike(
        cash_per_day, cost_bike, left=0, right=number_days),
          amount_for_bike(
        cash_per_day, two_bikes, left=0, right=number_days)
    )
