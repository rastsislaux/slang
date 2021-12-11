from    slang.dicts   import  Dicts
from    slang.keyword import  Keyword
from    slang.type    import  Type
from    slang.utils   import  Utils
from    slang.method  import  Method

class Translators:

    """Contains translators for parts and the whole code"""

    @staticmethod
    def parameter(a: list):

        """Translates slang parameter declaration into python"""

        return a[1] + " : " + Dicts.types[a[0]]

    @staticmethod
    def parameters(a: list):

        """Translates bunch of parameters"""

        if a[0] == "nothing":
            return ""
        i = 0
        result = ""

        while i < len(a):
            result += Translators.parameter(a[i:i + 2])
            if i != len(a) - 2:
                result += ", "
            i += 2

        return result

    @staticmethod
    def code(lines: list) -> str:

        r = ""
        tabs = ""

        for line in lines:

            if not line:
                r += "\n"
                continue

            tokens = line.split()

            if tokens[0] not in [Keyword.ELSE]:
                r += tabs

            match tokens[0]:

                # Translating keywords

                case Keyword.IMPORT:

                    if len(tokens) == 2:
                        r += "import " + ", ".join(tokens[1:]) + "\n"

                    else:
                        r += f"from {tokens[1]} import " + ", ".join(tokens[2:])

                case Keyword.INCLUDE:
                    with open(f"{tokens[-1]}.slang") as module_file:
                        module_code = module_file.read()
                    r += f"\n# Code from module {tokens[-1]}\n"
                    r += Translators.main(module_code, module = True)

                case Keyword.FUNC:
                    r += "def " + tokens[1] + "(" + \
                         Translators.parameters(tokens[3:-2]) + \
                         ") -> " + Dicts.types[tokens[-1]] + \
                         ":\n"
                    tabs += "\t"

                case Keyword.RETURN:
                    r += "return " + tokens[-1] + "\n"

                case Keyword.END:
                    tabs = tabs[:-1]
                    r += "\n"

                case Keyword.IF:
                    r += "if " + tokens[1] + ":\n"
                    tabs += "\t"

                case Keyword.ELSE:
                    tabs = tabs[:-1]
                    r += tabs + "else:\n"
                    tabs += "\t"

                case Keyword.WHILE:
                    r += "while " + tokens[1] + ":\n"
                    tabs += "\t"

                case Keyword.BREAK:
                    r += "break\n"

                case Keyword.SET:
                    r += tokens[1] + " = " + tokens[2] + "\n"

                case Keyword.FOREACH:
                    r += f"for {tokens[1]} in {tokens[3]}:\n"
                    tabs += "\t"

                # Translating methods

                case Method.PRINT:
                    r += "print(str(" + ") + str(".join(tokens[1:]) + "), end = '')\n"

                case Method.INPUT:
                    r += tokens[-1] + " = " + "type(" + tokens[-1] + ")(" + tokens[0] +\
                         "(" + ", ".join(tokens[1:-2]) + "))\n"

                case Method.APPEND:
                    r += tokens[-2] + ".append(" + tokens[-1] + ")\n"

                # Translating variable declarations

                case Type.INT:
                    r += tokens[-1] + " = 0\n"

                case Type.BOOL:
                    r += tokens[-1] + " = False\n"

                case Type.FLOAT:
                    r += tokens[-1] + " = 0.0\n"

                case Type.STR:
                    r += tokens[-1] + " = ''\n"

                case Type.LIST:
                    r += tokens[-1] + " = []\n"

                case Type.DICT:
                    r += tokens[-1] + " = {}\n"

                case _:
                    if (len(tokens) > 1 and tokens[-2] == "->"):
                        r += tokens[-1] + " = " + tokens[0] + "(" + ", ".join(tokens[1:-2]) + ")\n"
                    else:
                        r += tokens[0] + "(" + ", ".join(tokens[1:]) + ")\n"

        return r

    @staticmethod
    def main(source_code: str, module = False) -> str:

        """Translates slang into python"""

        result = ""

        # Refactoring the code

        source_text = Utils.strip_lines(
                      Utils.remove_comments(
                      Utils.remove_newlines(
                          source_code
                      )).split(';'))

        result += Translators.code(source_text)

        if not module:
            result += "if __name__ == \"__main__\":\n\tmain()\n"

        return result
