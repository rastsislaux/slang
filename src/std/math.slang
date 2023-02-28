/*
    THIS FILE IS A PART OF SLANG STANDARD LIBRARY.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.
*/

include std.types

macro std.math.pow
    $base swap &
    $exponent swap &

    // if exponent = 1, return base
    $exponent @ 1 = if
        $base @ return
    fi

    // if exponent = 0 return 1
    $exponent @ 0 = if
        1 return
    fi

    // if exponent < 0, return None
    $exponent @ 0 > if
        None return
    fi

    $answer $base @ &

    true while
        $answer dup @ $base @ * &
        $exponent dup @ -- &
        $exponent @ 1 <
    do
    $answer @
end

/*
HOW IT USED TO LOOK LIKE WITHOUT VARIABLES:
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

end */

macro std.math.fact

    dup 1 = swap dup 0 = swap rot or if
        drop
        1 return
    fi

    dup 0 > if
        drop
        None return
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

macro std.math.abs using std.types namespaces
    to-str!
    "math.fabs(" + ")" swap +
    "math" swap pycall
end

macro std.math.floor using std.types namespaces
    to-int!
end

macro std.math.ceil using std.types namespaces
    to-int! 1 +
end

macro std.math.round using std.types namespaces
    "" "round(stack.pop(), 0)" pycall to-int!
end

macro std.math.dround
    // {decimals} {number} std.math.dround!
    "" "round(stack.pop(), stack.pop())" pycall
end

macro std.math.log
    // {base} {a} std.math.log!
    "math" "math.log(stack.pop(), stack.pop())" pycall
end

macro std.math.ln
    "math" "math.log(stack.pop())" pycall
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