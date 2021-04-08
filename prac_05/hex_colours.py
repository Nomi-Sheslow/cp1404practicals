"""
CP1404/CP5632 Practical
Hex colours in a dictionary
get valid user input
"""

COLOUR_TO_HEX = {"black": "#000000", "brown": "#a52a2a", "VioletRed": "#d02090", "white": "#ffffff",
"SteelBlue": "#4682b4", "SlateBlue": "#6a5acd", "SeaGreen1": "#54ff9f", "salmon": "#fa8072", "RoyalBlue4": "#27408b",
"RosyBrown1": "#ffc1c1"}

colour_name = input("Colour name: ")
while colour_name != "":
    if colour_name in COLOUR_TO_HEX:
        print(f"{colour_name} hex code is {COLOUR_TO_HEX[colour_name]}")
    else:
        print("Not in dictionary")
    colour_name = input("Colour name: ")
