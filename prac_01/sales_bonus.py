sales = float(input("Enter sales: $"))
while sales > -1:
    if 0 < sales < 1000:
        bonus = sales * 0.1
        print("Sales bonuis is : $ {:.2f} ".format(bonus))
        sales = float(input("Enter sales: $"))
    elif 1000 <= sales:
        bonus = sales * 0.15
        print("sales bonuis is : $ {:.2f} ".format(bonus))
        sales = float(input("Enter sales: $"))
