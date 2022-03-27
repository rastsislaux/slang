include std.io
include std.types

macro no-recursion using std.types namespaces
    $number swap &
    $system swap &

    $result "" &
    ($system @ $number @ >=) while
        $result dup @
        ($system @ $number @ %)to-str!
        + &
        $number dup @ $system @ swap / to-int! &
    ($system @ $number @ >=) do

    $result dup @
    ($number @)to-str! + &

    $result @
end

macro recursion using std.types namespaces
    $number swap &
    $system swap &

    ($system @ $number @ <) if
        ($number @)to-str! return
    fi

    $result "" &
    ($system @ $number @ %)to-str!

    (
        $system @,
        ($system @ $number @ /)to-int!
    )recursion!

    +
end

macro main using std.io namespaces
    (2, 154)no-recursion!
    (2, 154)recursion!
    popln! popln!
end