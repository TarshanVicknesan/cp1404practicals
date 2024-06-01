# display menu
# get choice
# while choice != <quit option>
#     if choice == <first option>
#         <do first task>
#     else if choice == <second option>
#         <do second task>
# ...
#     else if choice == <n-th option>
#         <do n-th task>
#     else
#         display invalid input error message
#     display menu
#     get choice
# <do final thing, if needed>

def main():
    """main function to print out menu and get input from user (used standard menu pattern provided)"""
    score = None

    MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

    choice = None  # Initializing choice variable

    while choice != "Q":
        print(MENU)  # Moved the printing of menu here

        choice = input(">>> ").upper()

        if choice == "G":
            score = validate_score()
        elif choice == "P":
            if score is not None:
                result = evaluate_score(score)
                print(f"The result is: {result}")
            else:
                print("There doesn't seem to be a score, use 'G' to get a valid score.")
        elif choice == "S":
            if score is not None:
                show_stars(score)
            else:
                print("No score inputted, use 'G' to get a valid score.")
        elif choice != "Q":
            print("Invalid choice")

    print("Finished.")
    print("Goodbye!")


def evaluate_score(score):
    """reused score.py evaluate score function to get comment on score"""
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


def validate_score():
    """validate score function to perform error-checking on scores"""
    valid_score = False
    while not valid_score:
        user_input = input("Enter a valid score (0-100 inclusive): ")

        if user_input.isdigit():
            score = int(user_input)
            if 0 <= score <= 100:
                print("Valid score:", score)
                valid_score = True
            else:
                print("Invalid score. Please enter a value between 0 and 100.")
        else:
            print("Invalid input. Please enter a valid integer score.")

    return score


def show_stars(score):
    """simple function to show the amount of stars(asterisks) depending on score inputted"""
    print("*" * score)


main()
