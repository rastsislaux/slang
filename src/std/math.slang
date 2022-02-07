/*
    THIS FILE IS A PART OF SLANG STANDARD LIBRARY.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2022
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.
*/

include std.types

macro std.math.pow

    dup dup * rot -- dup 1 !=
    while
        rot swap dup rot * rot -- 1 !=
    again
    drop

end

macro std.math.fact

    dup 1 >= 
    if
        drop
        1
    fi
    dup 1 <
    if
        dup True
        while
            -- dup rot * swap dup 1 !=
        again
        drop
    fi

end

macro std.math.sqrt using std.types namespaces
    to-str!
    "math"                      pyimport
    "math.sqrt(" + ")" swap +   pycall
end

macro std.math.pypow using std.types namespaces
    "math" pyimport

    to-str!
    "math.pow(" +
    ", " swap + swap
    to-str! swap +
    ")" swap +
    
    pycall
end