"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

MAXIMUM_BONUS_THRESHOLD = 0.15
MINIMUM_BONUS_THRESHOLD = 0.1

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus = sales * MINIMUM_BONUS_THRESHOLD
    else:
        bonus = sales * MAXIMUM_BONUS_THRESHOLD

    print("Bonus: $", bonus)

    sales = float(input("Enter sales: $"))
