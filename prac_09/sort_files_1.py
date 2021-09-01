import shutil
import os


def main():
    os.chdir('FilesToSort')

    file_types = []

    for filename in os.listdir('.'):
        split_filename = filename.split(".")
        if split_filename[1] not in file_types:
            file_types.append(split_filename[1])
    try:
        for file_type in file_types:
            os.mkdir(f"{file_type}")
    except FileExistsError:
        pass

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        split_filename = filename.split(".")
        shutil.move(filename, f'{split_filename[1]}/')


main()
