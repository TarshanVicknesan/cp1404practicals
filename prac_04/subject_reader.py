"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data_list = []  # Initialize an empty list to store the data
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data_list.append(parts)  # Append the processed data to the list
    input_file.close()
    return data_list


def display_subject_details(data_list):
    """Display subject details in the specified format."""
    for subject_data in data_list:
        subject = subject_data[0]
        lecturer = subject_data[1]
        num_students = subject_data[2]
        print(f"{subject} is taught by {lecturer} and has {num_students} students")


main()

