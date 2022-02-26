#! /bin/python3.10 

# THIS FILE IS A PART OF SLANG INTERPRETER.
# AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
# DATE: 06.02.2022
# VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.


import sys
import pickle

from slang import Utils, Interm, Macro, Interpreter


def compile_to_bytecode(given_src_code: str):
    src_code = given_src_code
    src_code = Utils.remove_comments(src_code) \
        .split()
    src_code = Utils.unite_string_literals(src_code)
    tokens = Interm.parse_tokens(src_code)
    macros = Macro.generate_macros(tokens)
    return macros


def save_pickled(_object, path: str = "out.slangc"):
    with open(path, 'wb') as com_file:
        com_file.write(pickle.dumps(_object))


def open_pickled(path: str):
    with open(path, 'rb') as src_file:
        macros = pickle.loads(src_file.read())
    return macros


def main(args: list):

    match args[0]:

        case "com":

            with open(args[1], 'r') as src_file:
                src_code = src_file.read()
            macros = compile_to_bytecode(src_code)

            path = "out.slangc"
            if len(args) > 2:
                path = args[2]
            save_pickled(macros, path)

        case "exe":

            macros = open_pickled(args[1])
            Interpreter.interpret(macros, "main")

        case "run":

            with open(args[1], 'r') as src_file:
                src_code = src_file.read()
            macros = compile_to_bytecode(src_code)
            Interpreter.interpret(macros, "main")


if __name__ == "__main__":
    main(sys.argv[1:])
