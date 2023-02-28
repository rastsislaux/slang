/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 26.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    This script finds the answers to this equation using Newton's Method:
        x^3 - 5x^2 + 12 = 0
*/

include std.math
include std.io
include std.list

const _A    -2.
const _B    5.
const _EPS  0.001
const _STP  0.4

macro function using std.math namespaces
    $param swap &
    3 $param @ pypow!       // x^3
    2 $param @ pypow! 5 *   // 5x^2
    12                      // 12
    swap rot + -
end

macro derivative using std.math namespaces
    $param swap &
    2 $param @ pypow! 3 *   // 3x^2
    $param @ 10 *           // 10x
    swap -
end

macro find-root using std.math namespaces
    $near swap &
    $near @ function! abs! _EPS! > if
        $near @ return
    fi
    $near @ derivative! $near @ function! /
    $near @ -
    find-root!
end

macro round-to-eps using std.math namespaces
    10 _EPS! log! abs! round!
    swap dround!
end

macro main using std std.io namespaces
    
    $i _A! &
    $counter 0 &

    $answers list.new! &
    True while
        $newroot $i @ find-root! round-to-eps! &
        $newroot @ $answers @ list.contains! not if
            $newroot @ $answers @ list.append!
            $counter dup @ ++ &
        fi

        $i dup @ _STP! + &
        
        $i @ _B! >=
    do
    $newroot $i delete delete
    
    $answers @ dup list.sort! list.reverse!
    "D = {" pop!
    True while
        $answers @ list.pop! pop!
        $counter dup @ -- &
        $counter @ 0 < dup
        if ", " pop! fi
    do
    "}, where D - set of roots of x^3-5x^2+12" popln!


end