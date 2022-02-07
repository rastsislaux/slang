/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 07.02.2022
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    This program prints its own source code.
    Btw pycalls are bad :(
*/

include std.io

macro main using std.io namespaces

    "open('/home/rostislove/PycharmProjects/rpslang/examples/quine.slang')"
    pycall
    "stack.pop().read()"
    pycall

    popln!

end