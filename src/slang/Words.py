# THIS FILE IS A PART OF SLANG INTERPRETER.
# AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
# DATE: 26.02.2023
# VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.


from enum import Enum, auto


class Intrinsic(Enum):
    DUP = auto()
    ROT = auto()
    SWAP = auto()
    DROP = auto()
    OVER = auto()

    ADD = auto()
    SUB = auto()
    DIV = auto()
    MUL = auto()
    REM = auto()
    INC = auto()
    DEC = auto()

    NOT = auto()
    AND = auto()
    OR = auto()
    XOR = auto()

    LESS = auto()
    GREATER = auto()
    EQUAL = auto()
    GREATEREQUAL = auto()
    LESSEQUAL = auto()
    NOTEQUAL = auto()

    PYCALL = auto()

    PACK = auto()
    UNPACK = auto()
    DELETE = auto()


t = {
    "dup": Intrinsic.DUP,
    "rot": Intrinsic.ROT,
    "swap": Intrinsic.SWAP,
    "drop": Intrinsic.DROP,
    "over": Intrinsic.OVER,

    "+": Intrinsic.ADD,
    "-": Intrinsic.SUB,
    "/": Intrinsic.DIV,
    "*": Intrinsic.MUL,
    "%": Intrinsic.REM,
    "++": Intrinsic.INC,
    "--": Intrinsic.DEC,

    "not": Intrinsic.NOT,
    "and": Intrinsic.AND,
    "or": Intrinsic.OR,
    "xor": Intrinsic.XOR,

    "<": Intrinsic.LESS,
    ">": Intrinsic.GREATER,
    "=": Intrinsic.EQUAL,
    ">=": Intrinsic.GREATEREQUAL,
    "<=": Intrinsic.LESSEQUAL,
    "!=": Intrinsic.NOTEQUAL,

    "pycall": Intrinsic.PYCALL,

    "&": Intrinsic.PACK,
    "@": Intrinsic.UNPACK,
    "delete": Intrinsic.DELETE,
}


class Preprocessor(Enum):

    INCLUDE = auto()
    PATH = auto()
