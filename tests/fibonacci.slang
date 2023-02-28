/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    This program prints fibonacci sequence from 2 to 144.
*/

include std.io

const CAP 0x90

macro main using std.io namespaces

    1 1
    cycle:
        dup rot +
        dup putx!
        " (" pop! dup puti! ")" pop!
        dup CAP! >
        if
            ", " pop!
            cycle~
        fi
    drop drop
    "\n" pop!
    
end