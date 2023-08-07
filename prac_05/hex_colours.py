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


def main():
    color_name = input("Enter color name (press Enter to exit): ")
    while color_name:
        color_code = get_color_code(color_name)
        print(f"The hexadecimal code for {color_name} is {color_code}")
        color_name = input("Enter color name (press Enter to exit): ")


def get_color_code(color_name):
    # Convert the input color_name to uppercase for case-insensitivity
    color_name = color_name.upper()

    # Look up the color_name in the COLORS dictionary
    return COLORS.get(color_name, "Invalid color name")


main()
