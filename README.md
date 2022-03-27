# slang

Slang is an interpreted stack-based "programming language".

This project is a pathetic parody of [Porth](https://gitlab.com/tsoding/porth) by [Alexey Kutepov](https://www.youtube.com/c/TsodingDaily).

## Examples

Hello, World:

```slang
include std.io

macro main using std.io namespaces
    "Hello, world!\n" popln!
end
```

Simple program that prints numbers from 1 to 15 in an ascending order:

```slang
include std.io
const CAP 15
macro main using std.io namespaces
    0
    cycle:
        ++ println! 
        dup CAP! = not
        if cycle~ fi
    drop
end
```

## Quick start
Slang is an interpreted "programming language" so you need to configure interpretator before using it. Right now you just need to go to `src/pyslang` and change `LIBS_PATH` const to where you have slang std library. Maybe i'll create a configuration file later.

After you've done configuration, just run `pyslang run [path to program]`.

## Language reference

### Literals

#### Integer

Integer is a sequence of decimal digits that optionally starts with dash (`-`) to indicate a negative integer. When an integer is encountered it is pushed onto the stack.

Example:
```slang
5 10 +
```

This code pushes 5 and 10 onto the stack and then finds their sum with `+` operation.

#### String

String is a sequence of bytes between two `"`. No newlines are allowed, as Python supports unicode, slang does too.

Allowed escapes:
 - `\n` - new line
 - `\r` - carriage return
 - `\"` - double quote

When the interpretator encouters a string it is pushed onto the stack.

Example:
```slang
include std.io

macro main using std.io namespaces
   "Hello, world!" popln!
end
```

The `std.io.popln` macro expects any kind of value on the stack prints it and drops it. (<=> `std.io.println! drop`)

#### Other

There are other types supported, such as float and bool.
Actually, slang can work with any python type though it is not convinient as there's no suitable tools.

### Intrinsics (Built-in words)

#### Stack manipulation

| Name     | Signature         | Description                               |
| ---      | ---               | ---                                       |
| `dup`    | `a -- a a`        | duplicate an element on top of the stack  |
| `swap`   | `a b -- b a`      | swap 2 elements on the top of the stack   |
| `drop`   | `a b -- a`        | drops the top element of the stack        |
| `rot`    | `a b c -- c b a`  | rotate the top three stack elements       |
| `size`   | `a -- a s`        | pushes size of stack (int) on top of it   |

#### Comparison

| Name | Signature                | Description                                                  |
| ---  | ---                      | ---                                                          |
| `=`  | `a b -- [a == b : bool]` | checks if two elements on top of the stack are equal.        |
| `!=` | `a b -- [a != b : bool]` | checks if two elements on top of the stack are not equal.    |
| `> ` | `a b -- [a > b  : bool]` | applies the greater comparison on top two elements.          |
| `< ` | `a b -- [a < b  : bool]` | applies the less comparison on top two elements.             |
| `>=` | `a b -- [a >= b : bool]` | applies the greater or equal comparison on top two elements  |
| `<=` | `a b -- [a <= b : bool]` | applies the greater or equal comparison on top two elements. |

#### Communication with Python

| Name          | Signature                             | Description                |
| ---           | ---                                   | ---                        |
| `pyimport`    | `b [a: string] -- b`                  | imports a python library   |
| `pycall`      | `b [a: string] -- b [c: Object]`      | calls a python method      |

There are some more but I'm tired of that.

### Control Flow

#### if-condition

```slang
// -- snip --
<condition> if
    <body>
fi
// -- snip --
```

#### while-loop

```slang
// -- snip --
<start condition> while
    ...contents
<continue condition> do
// -- snip --
```

#### Include

```slang
// -- snip --
include package.file
// -- snip --
```
That code will include file from path `{LIBS_PATH}/package/file.slang`

#### Macros

```slang
// -- snip --
macro print-hello-world
    "Hello, world!\n" std.io.popln!
end
// -- snip --
macro main
    print-hello-world!
end
```

#### Constants
```slang
// -- snip --
const ONEHUNDRED 100
// -- snip --
```
