# L. Два велосипеда
# ID успешной посылки 66093576


def amount_for_bike(cash_per_day, cost_bike, left, right):
    if (right <= left and left != 0):
        return -1
    middle = (left + right) // 2
    if (cash_per_day[middle] >= cost_bike and (cash_per_day[middle - 1] < cost_bike or middle == 0)):
        return middle + 1
    elif cost_bike <= cash_per_day[middle]:
        return amount_for_bike(cash_per_day, cost_bike, left, middle)
    else:
        return amount_for_bike(cash_per_day, cost_bike, middle + 1, right)
    

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
