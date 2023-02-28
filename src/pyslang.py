#! /bin/python3.10 

# THIS FILE IS A PART OF SLANG INTERPRETER.
# AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
# DATE: 06.02.2023
# VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.


import os
import pickle
import json
import argparse
from pprint import pprint
from slang import Compiler, Interpreter


def save_pickled(_object, path: str = "out.sx"):
    with open(path, 'wb') as com_file:
        com_file.write(pickle.dumps(_object))


def open_pickled(path: str):
    with open(path, 'rb') as src_file:
        macros = pickle.loads(src_file.read())
    return macros


def parse_args():
    parser = argparse.ArgumentParser(description=
                                     """
                                     pyslang is a slang interpreter. Slang source code files have .slang expansion
                                     and slang bytecode (compiled programs) have .sx expansion.
                                     """)
    parser.add_argument("command",
                        choices=["run", "com", "exe"],
                        help="mode (run - interpret, com - compile, exe - execute bytecode)")
    parser.add_argument("file", type=str, help="path to source code")
    parser.add_argument("-i", "--intermediate", help="print the intermediate representation", action="store_true")
    parser.add_argument("-o", "--out", help="path to save compiled file (only with com)",
                        default="out.sx")
    return parser.parse_args()


def main():

    args = parse_args()
    match args.command:

        case "com":

            dir_path = os.path.dirname(os.path.realpath(__file__))
            with open(dir_path + "/" + "pyslang.json", 'r') as config_file:
                config = json.loads(config_file.read())

            with open(args.file, 'r') as src_file:
                src_code = src_file.read()
            macros = Compiler.compile_to_bytecode(src_code, config["stdlib-path"])
            if args.intermediate:
                pprint(macros)
            path = args.out
            save_pickled(macros, path)

        case "exe":

            macros = open_pickled(args.file)
            if args.intermediate:
                pprint(macros)
            Interpreter.interpret(macros, "main")

        case "run":

            dir_path = os.path.dirname(os.path.realpath(__file__))
            with open(dir_path + "/" + "pyslang.json", 'r') as config_file:
                config = json.loads(config_file.read())

            with open(args.file, 'r') as src_file:
                src_code = src_file.read()
            macros = Compiler.compile_to_bytecode(src_code, config["stdlib-path"])
            if args.intermediate:
                pprint(macros)
            Interpreter.interpret(macros, "main")


if __name__ == "__main__":
    main()
