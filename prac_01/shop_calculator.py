DISCOUNT = 0.1

number_items = int(input("Number of items: "))

total_price = 0

while number_items < 0:
    print("Invalid number of items!")
    number_items = int(input("Number of items: "))

for i in range(number_items):
    price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    discount = total_price * DISCOUNT
    total_price -= discount

print(f"Total price for {number_items} items is ${total_price:.2f}")
