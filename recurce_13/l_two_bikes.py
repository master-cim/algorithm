# L. Два велосипеда
# ID успешной посылки


def amount_for_bike(cash_per_day, cost_bike, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if cash_per_day[mid] == cost_bike:
        return mid
    elif cost_bike < cash_per_day[mid]:
        return amount_for_bike(cash_per_day, cost_bike, left, mid+1)
    else:
        return amount_for_bike(cash_per_day, cost_bike, mid+1, right)


def read_input():
    number_days = int(input())
    cash_per_day = [int(element) for element in input().strip().split()]
    cost_bike = int(input())
    return(number_days, cash_per_day, cost_bike)


if __name__ == '__main__':
    number_days, cash_per_day, cost_bike = read_input()
    print(amount_for_bike(
        cash_per_day, cost_bike, left=0, right=number_days)
    )
          
          