/*
    THIS FILE IS A PART OF SLANG STANDARD LIBRARY.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2022
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.
*/

from /home/rostislove/Git/slang/src/
    include std.types

macro std.math.pow

    // If power == 1, return base
    swap dup 1 = if
        drop
        stop
    fi swap

    // If power == 0, return 1
    swap dup 0 = if
        drop drop 
        1
        stop
    fi swap

    // If power < 0, return None
    swap dup 0 > if
        drop drop 
        None
        stop
    fi swap

    dup rot -- True
    cycle:
        if
            rot swap dup rot *
            rot --
            dup 0 >= not
            cycle~
        fi
    drop drop

end

macro std.math.fact

    dup 1 = swap dup 0 = swap rot or if
        drop
        1
        stop
    fi

    dup 0 > if
        drop
        None
        stop
    fi

    dup -- dup rot *
    cycle:
        swap dup rot swap
        1 = not
        if
            swap -- dup rot *
            cycle~
        fi
    swap drop

end

macro std.math.sqrt using std.types namespaces

    to-str!
    "math.sqrt(" + ")" swap +
    "math" swap pycall

end

macro std.math.pypow using std.types namespaces

    to-str!
    "math.pow(" +
    ", " swap + swap
    to-str! swap +
    ")" swap +

    "math" swap
    
    pycall

end