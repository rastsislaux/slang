/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 07.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    Includes from included file work properly (check src/std.slang)
*/

include std

macro main
    "Hello, world!" std.types.to-bool! std.io.popln!
end