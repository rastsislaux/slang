/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    This is an example of using std.math package.
*/

include std.io
include std.math

macro main using std.io std.math namespaces

    // These are functions written in slang, without pycalls
    5       fact!   popln!
    3 5     pow!    popln!
    // They work though they have limitations. For instance, pow! returns None if power is less than 0.
    -2 5    pow!    popln!
    
    // There are function that use pycalls
    16      sqrt!   popln!  // <=> math.sqrt(16)
    0.5 16  pypow!  popln!  // <=> math.pow(16, 0.5)

end