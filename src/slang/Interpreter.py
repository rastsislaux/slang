# THIS FILE IS A PART OF SLANG INTERPRETER.
# AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
# DATE: 26.02.2023
# VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.


import slang.Interm


def run_intrinsic(stack, intrinsic, variables: dict):

    match intrinsic:

        case slang.Words.Intrinsic.PYCALL:
            eval_target = stack.pop()
            modules = stack.pop()
            modules = modules.split()
            for module in modules:
                exec(f"import {module}")
            stack.append(eval(eval_target))

        case slang.Words.Intrinsic.INC:
            stack[-1] += 1

        case slang.Words.Intrinsic.DEC:
            stack[-1] -= 1

        case slang.Words.Intrinsic.ADD:
            stack.append(stack.pop() + stack.pop())

        case slang.Words.Intrinsic.SUB:
            stack.append(stack.pop() - stack.pop())

        case slang.Words.Intrinsic.MUL:
            stack.append(stack.pop() * stack.pop())

        case slang.Words.Intrinsic.DIV:
            stack.append(stack.pop() / stack.pop())

        case slang.Words.Intrinsic.REM:
            stack.append(stack.pop() % stack.pop())

        case slang.Words.Intrinsic.EQUAL:
            stack.append(stack.pop() == stack.pop())

        case slang.Words.Intrinsic.NOTEQUAL:
            stack.append(stack.pop() != stack.pop())

        case slang.Words.Intrinsic.GREATER:
            stack.append(stack.pop() > stack.pop())

        case slang.Words.Intrinsic.GREATEREQUAL:
            stack.append(stack.pop() >= stack.pop())

        case slang.Words.Intrinsic.LESSEQUAL:
            stack.append(stack.pop() <= stack.pop())

        case slang.Words.Intrinsic.LESS:
            stack.append(stack.pop() < stack.pop())

        case slang.Words.Intrinsic.NOT:
            stack[-1] = not stack[-1]

        case slang.Words.Intrinsic.OR:
            f = stack.pop()
            s = stack.pop()
            stack.append(f or s)

        case slang.Words.Intrinsic.XOR:
            f = stack.pop()
            s = stack.pop()
            stack.append(f ^ s)

        case slang.Words.Intrinsic.AND:
            f = stack.pop()
            s = stack.pop()
            stack.append(f and s)

        case slang.Words.Intrinsic.DUP:
            stack.append(stack[-1])

        case slang.Words.Intrinsic.SWAP:
            temp = stack[-1]
            stack[-1] = stack[-2]
            stack[-2] = temp

        case slang.Words.Intrinsic.ROT:
            temp = stack[-3]
            stack[-3] = stack[-1]
            stack[-1] = temp

        case slang.Words.Intrinsic.DROP:
            stack.pop()

        case slang.Words.Intrinsic.OVER:
            stack.append(stack.pop(0))

        case slang.Words.Intrinsic.PACK:
            content = stack.pop()
            destination = stack.pop()

            if destination.name not in variables:
                raise MemoryError("Writing to non-existing variable.")

            variables[destination.name] = content

        case slang.Words.Intrinsic.UNPACK:
            target = stack.pop().name
            if target not in variables:
                raise MemoryError("Reading from non-existing variable.")
            stack.append(variables[target])

        case slang.Words.Intrinsic.DELETE:
            target = stack.pop().name
            variables.pop(target)

        case _:
            raise NotImplementedError(f"Intrinsic <{intrinsic}> not implemented yet.")


def interpret(macros: dict, name: str, stack=[]):

    goto_points = {}
    variables = {}

    for i, token in enumerate(macros[name]):
        if isinstance(token, slang.Interm.GotoPoint):
            goto_points[token.name] = i

    i = 0
    while i < len(macros[name]):

        if isinstance(macros[name][i], slang.Interm.MacroCall):
            success = False
            for namespace in [""] + [nmspc + "." for nmspc in macros[name]._namespaces]:
                try:
                    interpret(macros, namespace + macros[name][i].name, stack)
                    success = True
                except KeyError:
                    pass
            if not success:
                raise NameError(f"Macro \"{macros[name][i].name}\" not found while interpreting.")

            i += 1
            continue

        if isinstance(macros[name][i], slang.Interm.OpPush):
            stack.append(macros[name][i].value)
            i += 1
            continue

        if isinstance(macros[name][i], slang.Interm.PushVar):
            if (macros[name][i].name not in variables):
                variables[macros[name][i].name] = macros[name][i].value
            stack.append(Variable(macros[name][i].name))

        if isinstance(macros[name][i], slang.Words.Intrinsic):
            run_intrinsic(stack, macros[name][i], variables)
            i += 1
            continue

        if isinstance(macros[name][i], slang.Interm.GotoCall):
            try:
                i = goto_points[macros[name][i].name]
            except:
                raise KeyError(f"Goto mark named `{macros[name][i].name}` not found.")
            i += 1
            continue

        if isinstance(macros[name][i], slang.Interm.IfStart):
            if not stack.pop():
                counter = 0
                success = False
                for j, token in enumerate(macros[name][i:]):
                    if isinstance(token, slang.Interm.IfStart):
                        counter += 1
                    if isinstance(token, slang.Interm.IfEnd):
                        counter -= 1
                    if counter == 0:
                        i = i + j
                        success = True
                        break
                if not success:
                    raise SyntaxError("Failed to jump over if statement.")
            else:
                i += 1
            continue

        if isinstance(macros[name][i], slang.Interm.OpStop):
            return

        i += 1


class Variable:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<slang.variable: {self.name}>"

    def __str__(self):
        return self.__repr__()


