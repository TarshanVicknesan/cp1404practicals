"""
CP1404/CP5632 Practical
"""

COLOURS = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUA": "#00ffff",
    "AQUAMARINE": "#7fffd4",
    "AZURE": "#f0ffff",
    "BEIGE": "#f5f5dc",
    "BISQUE": "#ffe4c4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#ffebcd",
    "BLUE": "#0000ff"
}
print(COLOURS)

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOURS.get(colour_name)}")
    colour_name = input("Enter a colour name: ")
