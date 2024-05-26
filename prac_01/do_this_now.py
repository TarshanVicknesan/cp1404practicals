# gift = int(input("Enter number of gifts: "))
# student = int(input("Enter number of students: "))
#
# gift_each_student = gift // student
# leftover_gifts = gift % student
#
# print(f"Gifts distributed to each student is {gift_each_student} and left over gifts amount to {leftover_gifts}")

# get item price
# ask user for whether if there is GST (Y/N)
# print final price

# GST = 0.09
#
# item_price = float(input("Enter item price: "))
#
# GST_price = item_price * GST
# final_price = GST_price + item_price
# print(f"Final Price: $ {final_price:.2f}")

# SECRET_NUMBER = 2
# number = int(input("Guess a number between 1 to 10: "))
#
# while number != SECRET_NUMBER:
#     print("Try Again")
#     number = int(input("Guess a number between 1 to 10: "))
# print("Good Job")

# total_age_num = 0
#
# age_num = int(input("How many ages to enter: "))
#
# for i in range(age_num):
#     age = int(input("Enter age: "))
#     total_age_num += age
#
# average = total_age_num / age_num
#
# print(total_age_num)
# print(average)

# total_age_num = 0
# count = 0
# age = int(input("Enter age: "))
#
# while age != -1:
#     total_age_num += age
#     count += 1
#     age = int(input("Enter age: "))
#
# average_age = total_age_num / count
#
#
# print(average_age)

for i in range(1, 4):
    for j in range(2, 10, 3):
        print(i, "-", j + i)
