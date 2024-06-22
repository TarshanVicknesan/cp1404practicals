def main():
    """
    Count occurrences of words in a string entered by the user.
    Outputs the counts sorted alphabetically and aligned properly.
    """
    user_string = input("Enter a string: ")
    word_list = user_string.lower().split()

    word_to_count = {}
    for word in word_list:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    sorted_word_counts = sorted(word_to_count.items())

    # Find the maximum word length for alignment
    max_length = max(len(word) for word, count in sorted_word_counts)

    # Print the word counts with proper alignment
    for word, count in sorted_word_counts:
        print(f"{word:{max_length}} : {count}")


main()
