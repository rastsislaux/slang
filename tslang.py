import os
import sys


from slang.translators import Translators as t


def main(args):

    """Shell implementation"""

    with open(args[1]) as file:
        src = file.read()

    translated = t.main(src)

    if len(args) == 3:
        save_path = args[2]
    else:
        save_path = "TEMP"

    with open(save_path, 'w') as file:
        file.write(translated)

    if len(args) < 3:
        os.system("python TEMP")
        os.system("rm TEMP")


if __name__ == "__main__":
    main(sys.argv)
