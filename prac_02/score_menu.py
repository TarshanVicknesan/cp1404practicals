def main():
    score = None

    MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(MENU)

    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score is not None:
                result = evaluate_score(score)
                print(f"The result is: {result}")
            else:
                print("No score available. Please use 'G' to get a valid score.")
        elif choice == "S":
            if score is not None:
                show_stars(score)
            else:
                print("No score available. Please use 'G' to get a valid score.")
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()

    print("Finished.")
    print("Farewell!")


def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    valid_score = False  # Use a flag variable to control the loop
    while not valid_score:
        user_input = input("Enter a valid score (0-100 inclusive): ")

        if user_input.isdigit():
            score = int(user_input)
            if 0 <= score <= 100:
                print("Valid score:", score)
                valid_score = True  # Set the flag to True to exit the loop
            else:
                print("Invalid score. Please enter a value between 0 and 100.")
        else:
            print("Invalid input. Please enter a valid integer score.")

    return score  # Return the valid score from the function


def show_stars(score):
    print("*" * score)


main()

# import random
#
#
# def main():
#     user_score = float(input("Enter your score: "))
#     result = evaluate_score(user_score)
#     print(result)
#
#     random_score = random.randint(0, 100)
#     result = evaluate_score(random_score)
#     print(f"Random score: {random_score}")
#     print(f"Result for random score: {result}")
#
#
# def evaluate_score(score):
#     if score < 0 or score > 100:
#         return "Invalid score"
#     elif score >= 90:
#         return "Excellent"
#     elif score >= 50:
#         return "Passable"
#     else:
#         return "Bad"
#
#
# main()
