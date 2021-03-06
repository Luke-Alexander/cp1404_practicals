"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo of os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # TODO: Try these options one at a time
        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)

    # Process all subdirectories using os.walk()
    os.chdir('..')  # '..' means to go 'up' one directory
    lyrics_path = os.getcwd()  # store the path so we can get back to it
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        os.chdir(directory_name)
        for filename in filenames:
            #    os.rename(filename, get_fixed_filename(filename))
            print(get_fixed_filename(filename))
        print(os.getcwd())
        os.chdir(lyrics_path)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    fixed = ""
    for i, letter in enumerate(new_name):
        if letter.islower() or letter.isupper():
            try:
                if new_name[i + 1].isupper():
                    fixed += letter
                    fixed += "_"
                else:
                    fixed += letter
            except IndexError:
                pass
        elif letter == "_":
            try:
                if new_name[i + 1].islower():
                    fixed += letter.upper()
                else:
                    fixed += letter
            except IndexError:
                pass
        else:
            fixed += letter

    return fixed


main()
