# Sample Output
# How many months? 5
#
# Enter income for month 1: 120
# Enter income for month 2: 245.4
# Enter income for month 3: 900
# Enter income for month 4: 1205.56
# Enter income for month 5: 12.35
#
# Income Report
# -------------
# Month  1 - Income: $    120.00         Total: $    120.00
# Month  2 - Income: $    245.40         Total: $    365.40
# Month  3 - Income: $    900.00         Total: $   1265.40
# Month  4 - Income: $   1205.56         Total: $   2470.96
# Month  5 - Income: $     12.35         Total: $   2483.31

"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes, num_months)


def print_income_report(incomes, num_months):
    """Print income report given a list of incomes and number of months."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
