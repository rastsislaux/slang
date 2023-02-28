/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 26.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    This is an example of including user source code.
*/

include std.io
from tests/etc/ include lib // use from to change include path

macro main using std.io namespaces
    1 lib.increase!
    popln!
end