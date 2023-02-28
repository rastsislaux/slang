# THIS FILE IS A PART OF SLANG INTERPRETER.
# AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
# DATE: 26.02.2023
# VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.


import slang.Interm


def find_used_macros(macros: list, macro="main") -> list:

    used_macros = []

    for token in macros[macro]:
        if isinstance(token, slang.Interm.MacroCall):

            success = False
            for namespace in [""] + [nmspc + "." for nmspc in macros[macro]._namespaces]:
                try:
                    if namespace + token.name == macro:
                        return used_macros + [macro]
                    used_macros += find_used_macros(macros, namespace + token.name)
                    success = True
                    break
                except KeyError:
                    pass
            if not success:
                raise NameError(f"Macro \"{token.name}\" not found while eliminating dead code.")

    return used_macros + [macro]


def eliminate_dead_code(macros: list) -> list:

    used = find_used_macros(macros)
    keys = list(macros.keys())
    result = macros.copy()

    for key in keys:
        if key not in used:
            result.pop(key)

    return result


def generate_macros(tokens: list) -> dict:

    macros = {}
    cur = None

    for token in tokens:
        if cur is None and isinstance(token, slang.Interm.MacroStart):
            cur = Macro(token.name, token.namespaces)
        elif cur is not None and isinstance(token, slang.Interm.MacroEnd):
            macros[cur._name] = cur
            cur = None
        elif cur is not None:
            cur._ops.append(token)    

    return eliminate_dead_code(macros)


class Macro:

    def __init__(self, name, namespaces):
        self._name = name
        self._namespaces = namespaces
        self._ops = []

    def __repr__(self):
        return f"<Macro: {self._name}, {self._namespaces}: {self._ops}>"

    def __str__(self):
        return self.__repr__()

    def add_op(self, token):
        self._ops.append(token)

    def __iter__(self):
        return self._ops.__iter__()

    def __len__(self):
        return len(self._ops)

    def __getitem__(self, item):
        return self._ops[item]
