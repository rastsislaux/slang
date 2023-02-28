# THIS FILE IS A PART OF SLANG INTERPRETER.
# AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
# DATE: 26.02.2023
# VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.


import re


def clear_decorative_symbols(text):
    new = ""
    in_string = False
    for symbol in text:
        if symbol == '"':
            in_string = not in_string
        if (symbol == ',' or symbol == ')' or symbol == '(') and not in_string:
            new += ' '
            continue
        new += symbol
    return new


def remove_comments(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)


def unite_string_literals(tokens: list) -> list:

    result = tokens.copy()
    uniting = None

    i = 0
    while i < len(result):

        if uniting != None:
            result[uniting] += ' ' + result.pop(i)
            i -= 1

        if uniting and result[i][-1] == '"':
            uniting = None

        if result[i][0] == '"' and (result[i][-1] != '"' or len(result[i]) == 1):
            uniting = i

        i += 1

    return result