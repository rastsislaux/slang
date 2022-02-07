/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2022
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    This program prints fibonacci sequence from 2 to 144.
*/

include std.io

const CAP 144

macro main using std.io namespaces

    1 1
    True while
        dup rot +
        print! ", " pop!
        dup CAP! >
    again

    drop drop
    "\n" pop!
    
end