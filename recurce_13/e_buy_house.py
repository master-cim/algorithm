# E. Покупка домов
# ID успешной посылки

def potential_shopping(price_house, cash,):
    if cash < 0:
        return 1
    
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
    input_list = list(map(int, input().split()))
    num_views = input_list[0]
    cash = input_list[1]
    price_house = sorted(list(map(int, input().split())))
    return num_views, cash, price_house


if __name__ == '__main__':
    num_views, cash, price_house = read_input()
    print(price_house, cash, left=0, right=num_views)
    print(amount_for_bike(
        cash_per_day, cost_bike, left=0, right=number_days)