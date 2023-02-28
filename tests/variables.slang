/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 25.03.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    Introduced variables.
*/

include std.io

const CAP 15

macro main using std.io namespaces

    $number 0 & // Use ${variable name} to allocate memory (when variable first introduced)
                // Use '&' intrinsic to store some data to that memory

    cycle:

        $number @ ++ println! // Use ${variable name} to get a pointer to value
                              // Use '@' intrinsic to get the value

        $number swap &
        $number @ CAP! != if
            cycle~
        fi

    $number delete // use `delete` keyword to clear memory

    $hw "Hello, world!" & // variables have a dynamic typing
    $hw @ popln!
    $hw delete

end