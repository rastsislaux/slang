/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2022
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    This program prints all numbers from 1 to 15.
*/

include std.io

const CAP       15
const print     std.io.print!
const pop       std.io.pop!

macro main

    0 True
    while
        ++ dup print!
        ", " pop!
        CAP! !=
    again
    drop
    "\n" pop!
    
end