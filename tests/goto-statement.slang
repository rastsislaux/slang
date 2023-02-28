/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    Testing goto to any part of macro
*/

include std.io

macro main using std.io namespaces

    "Hello, world!" popln!
    token-to-go-to~ // Goto operation is used before setting goto point.

    "This text should not be printed." popln!

    token-to-go-to: // But since interpretator checks for gotos
                    // before running macro it works

    "This should be printed." popln!

end