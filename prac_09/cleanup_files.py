"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    previous_character = ""
    characters = []
    for i, character in enumerate(new_name):
        new_character = new_name[i]
        if previous_character.islower() and character.isupper() and previous_character != "":
            new_character = f"_{character}"
        if previous_character.isupper() and character.isupper():
            new_character = f"_{character}"
        if previous_character == "_" and character.islower():
            new_character = character.upper()
        if previous_character == " ":
            new_character = "_"
        if previous_character == "(" and character.islower():
            new_character = character.upper()
        previous_character = new_character
        characters.append(new_character)
    new_name = ''.join(characters[0:len(characters)])
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        for filename in filenames:
            if os.path.isdir(filename):
                continue
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            os.path.join(directory_name, filename)
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))
        print("(Current working directory is: {})".format(os.getcwd()))


demo_walk()
