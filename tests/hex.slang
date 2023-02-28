/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    Testing hexidecimal literals.
*/

include std.io

macro main using std.io namespaces

    0x0000FF // Hex literals are supported.

    dup puti! "\n" pop!  // puti - print as int
    dup putc! "\n" pop!  // putc - print as char
    dup putb! "\n" pop!  // putb - print as bool
    dup putx! "\n" pop!  // putx - print as hex
    dup putf! "\n" pop!  // putf - print as float

end