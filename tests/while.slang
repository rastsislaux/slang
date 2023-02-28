/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 26.03.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    Introduced while keyword.
*/

include std.io

const CAP 15

macro main using std.io namespaces

    $number 0 &
    True while // While keyword needs a boolean, if true - while block will be executed, false - skip
        $number @ ++ println!
        $number swap &

        True while  // Whiles can be nested
            "Print once" println!
            False
        do

        $number @ CAP! != // Putting a boolean in the end (true - execute again, false - stop)
    do

end