/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2022
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    This program prints all numbers from 1 to 15.
*/

include std.io // adfsdf

const CAP       15

macro main using std.io namespaces

    0
    cycle:
        ++ println! 
        dup CAP! = not
        if cycle~ fi
    drop

end