"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """main function used to get user input of their score and adds the option to request for a random score"""
    user_score = float(input("Enter your score: "))
    result = evaluate_score(user_score)
    print(result)

    random_score = random.randint(0, 100)
    result = evaluate_score(random_score)
    print(f"Random score: {random_score}")
    print(f"Result for random score: {result}")


def evaluate_score(score):
    """evaluate score function to return grade/comment after input is given"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
