# THIS FILE IS A PART OF SLANG INTERPRETER.
# AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
# DATE: 26.02.2023
# VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.


import slang.Words
from slang.Utils import remove_comments, unite_string_literals, clear_decorative_symbols


class ParseError(Exception):
    pass


def parse_tokens(str_tokens: list, std_path: str = "~/.slang/") -> list:
    tokens = []
    while_stack = []
    path = std_path
    i = 0
    while i < len(str_tokens):

        try:
            tokens.append(OpPush(try_parse_push(str_tokens[i])))
            i += 1
            continue
        except ParseError:
            pass

        if str_tokens[i] == "from":
            path = str_tokens[i+1]
            i += 2
            continue

        if str_tokens[i] == "include":
            lib = path + str_tokens[i+1].replace(".", "/") + ".slang"
            with open(lib) as lib_file:
                lib_code = lib_file.read()
            lib_code = remove_comments(lib_code)
            lib_code = clear_decorative_symbols(lib_code)
            lib_code = lib_code.split()
            lib_code = unite_string_literals(lib_code)
            str_tokens = str_tokens[0:i] + lib_code + str_tokens[i+2:]
            continue

        if str_tokens[i] == "macro":
            j = i + 1
            namespaces = []
            if str_tokens[i+2] == "using":
                j = i + 3
                while str_tokens[j] != "namespaces":
                    namespaces.append(str_tokens[j])
                    j += 1
            tokens.append(MacroStart(str_tokens[i+1], namespaces))
            i = j + 1
            continue

        if str_tokens[i] == "const":
            tokens.append(MacroStart(str_tokens[i+1], []))
            tokens.append(OpPush(try_parse_push(str_tokens[i+2])))
            tokens.append(MacroEnd())
            i += 3
            continue

        if str_tokens[i] == "end":
            tokens.append(MacroEnd())
            i += 1
            continue

        if str_tokens[i] == "if":
            tokens.append(IfStart())
            i += 1
            continue

        if str_tokens[i] == "while":
            tokens.append(GotoPoint(f"WHILE_START_{i}"))
            tokens.append(slang.Words.Intrinsic.NOT)
            tokens.append(IfStart())
            tokens.append(GotoCall(f"WHILE_END_{i}"))
            tokens.append(IfEnd())
            while_stack.append(i)
            i += 1
            continue

        if str_tokens[i] == "do":
            goto_id = while_stack.pop()
            tokens.append(GotoCall(f"WHILE_START_{goto_id}"))
            tokens.append(GotoPoint(f"WHILE_END_{goto_id}"))
            i += 1
            continue

        if str_tokens[i] == "fi":
            tokens.append(IfEnd())
            i += 1
            continue

        if str_tokens[i] == "return":
            tokens.append(OpStop())
            i += 1
            continue

        if str_tokens[i][-1] == "!":
            tokens.append(MacroCall(str_tokens[i][:-1]))
            i += 1
            continue

        if str_tokens[i][-1] == ":":
            tokens.append(GotoPoint(str_tokens[i][:-1]))
            i += 1
            continue

        if str_tokens[i][-1] == "~":
            tokens.append(GotoCall(str_tokens[i][:-1]))
            i += 1
            continue

        if str_tokens[i][0] == "$":
            tokens.append(PushVar(str_tokens[i][1:]))
            i += 1
            continue

        if str_tokens[i] in slang.Words.t.keys():
            tokens.append(slang.Words.t[str_tokens[i]])
            i += 1
            continue

        raise ParseError(f"Unknown word: \"{str_tokens[i]}\".")

    return tokens


def try_parse_push(token: str):

    result = token

    if token in ["True", "true"]:
        return True
    if token in ["False", "false"]:
        return False

    if token == "None":
        return None

    try:
        result = int(result)
        return result
    except ValueError:
        pass

    try:
        result = int(result, 16)
        return result
    except ValueError:
        pass

    try:
        result = float(result)
        return result
    except ValueError:
        pass

    if token[0] == '"' and token[-1] == '"':

        token = token.replace("\\n", "\n")
        token = token.replace("\\r", "\r")
        token = token.replace("\\t", "\t")
        token = token.replace("\\\"", "\"")

        return token[1:-1]

    raise ParseError("Failed to parse as push op.")


class IfStart:

    def __repr__(self):
        return f"<If: start>"

    def __str__(self):
        return self.__repr__()


class IfEnd:

    def __repr__(self):
        return f"<If: end>"

    def __str__(self):
        return self.__repr__()



class WhileStart:

    def __repr__(self):
        return f"<While: start>"

    def __str__(self):
        return self.__repr__()


class WhileEnd:

    def __repr__(self):
        return f"<While: end>"

    def __str__(self):
        return self.__repr__()


class GotoPoint:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<GotoPoint: {self.name}>"

    def __str__(self):
        return self.__repr__()


class GotoCall:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<GotoCall: {self.name}>"

    def __str__(self):
        return self.__repr__()



class MacroCall:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<MacroCall: {self.name}>"

    def __str__(self):
        return self.__repr__()


class MacroStart:

    def __init__(self, name: str, namespaces: list):
        self.name = name
        self.namespaces = namespaces

    def __repr__(self):
        return f"<MacroStart: {self.name}, {self.namespaces}>"

    def __str__(self):
        return self.__repr__()


class MacroEnd:

    def __repr__(self):
        return f"<MacroEnd>"

    def __str__(self):
        return self.__repr__()


class OpPush:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"<OpPush: {self.value}>"

    def __str__(self):
        return self.__repr__()


class OpStop:

    def __repr__(self):
        return f"<OpStop>"

    def __str__(self):
        return self.__repr__()

class PushVar:

    def __init__(self, name):
        self.name = name
        self.value = None

    def __repr__(self):
        return f"<PushVar: {self.name}>"

    def __str__(self):
        return self.__repr__()