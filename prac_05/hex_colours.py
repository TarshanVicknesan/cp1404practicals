COLORS = {
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

colour_name = input("Enter a colour name: ")
while colour_name != "":
    # Note: using the get dictionary method
    # means you will get None if the key is not found
    print(f"The code for \"{colour_name}\" is {COLORS.get(colour_name)}")
    colour_name = input("Enter a colour name: ")