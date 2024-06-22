# # TODO: Reformat this file so the dictionary code follows PEP 8 convention
# CODE_TO_NAME = {
#     "QLD": "Queensland",
#     "NSW": "New South Wales",
#     "NT": "Northern Territory",
#     "WA": "Western Australia",
#     "ACT": "Australian Capital Territory",
#     "VIC": "Victoria",
#     "TAS": "Tasmania"
# }
#
# # Loop print the dictionary
# for code, name in CODE_TO_NAME.items():
#     print(f"{code:<3} is {name}")
#
# state_code = input("Enter short state: ").upper()
# while state_code != "":
#     try:
#         # Try to print the state name using the EAFP approach
#         print(f"{state_code} is {CODE_TO_NAME[state_code]}")
#     except KeyError:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()

# Define a dictionary with some color names and their corresponding hexadecimal codes
COLOUR_CODES = {
    'absolute zero': '#0048ba',
    'acid green': '#b0bf1a',
    'aliceblue': '#f0f8ff',
    'alizarin crimson': '#e32636',
    'amaranth': '#e52b50',
    'amber': '#ffbf00',
    'amethyst': '#9966cc',
    'antiquewhite': '#faebd7',
    'antiquewhite1': '#ffefdb',
    'antiquewhite2': '#eedfcc'
}

# Loop to print the dictionary
for name, code in COLOUR_CODES.items():
    print(f"{name:<14} is {code}")

# Prompt the user to enter a color name
color_name = input("Enter color name: ").lower()
while color_name != "":
    try:
        # Try to print the color code using the EAFP approach
        print(f"{color_name} is {COLOUR_CODES[color_name]}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").lower()
