/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 26.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    This is an example of using std.list
*/

include std.io
include std.list

macro main using std namespaces
    
    $array list.new! &

    $i 0 &
    True while
        $i @ $array @ list.append!
        $i dup @ ++ &
        $i @ 16 !=
    do

    5 $array @ list.ipop! io.popln!
    $array @ io.popln!
    
end