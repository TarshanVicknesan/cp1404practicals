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



