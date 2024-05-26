"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

"PSEUDOCODE"

get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing

"""
HIGHER_BONUS_THRESHOLD = 0.15
LOWER_BONUS_THRESHOLD = 0.1

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * LOWER_BONUS_THRESHOLD
    else:
        bonus = sales * HIGHER_BONUS_THRESHOLD
        print("Bonus: $", bonus)
        sales = float(input("Enter sales: $"))

