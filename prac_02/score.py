import random


def main():
    user_score = float(input("Enter your score: "))
    result = evaluate_score(user_score)
    print(result)

    random_score = random.randint(0, 100)
    result = evaluate_score(random_score)
    print(f"Random score: {random_score}")
    print(f"Result for random score: {result}")


def evaluate_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
