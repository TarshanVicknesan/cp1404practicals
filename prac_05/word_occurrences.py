"""
CP1404/CP5632 Practical
"""

word_to_count = {}
user_string = input("Enter a string: ")
word_list = user_string.split()

for word in word_list:
    lowercase_word = word.lower()
    word_to_count[lowercase_word] = word_to_count.get(lowercase_word, 0) + 1

sorted_word_counts = sorted(word_to_count.items())

maximum_word_length = max(len(word) for word, _ in sorted_word_counts)
for word, count in sorted_word_counts:
    print(f"{word:{maximum_word_length}} : {count}")



