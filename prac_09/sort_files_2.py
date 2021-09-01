import shutil
import os


def main():
    os.chdir('FilesToSort')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    file_types = os.listdir('.')

    for file_type in file_types:
        new_directory = input(f"What category would you like to sort {file_type} files into? ")
        try:
            os.mkdir(f"{new_directory}")
        except FileExistsError:
            pass
        for filename in os.listdir(f"./{file_type}"):
            shutil.move(os.path.join(f"./{file_type}", filename), f"./{new_directory}")
        os.rmdir(f"./{file_type}")


main()
