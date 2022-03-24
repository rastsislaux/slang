from /home/andrey/Programming/slang/src/
    include std.io

const CAP 15

macro main using std.io namespaces

    $number 0 &
    cycle:
        $number @ ++ println!
        $number swap &
        $number @ CAP! != if
            cycle~
        fi

end