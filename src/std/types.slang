/*
    THIS FILE IS A PART OF SLANG STANDARD LIBRARY.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.
*/

macro std.types.to-str
    "" "str(stack.pop())"
    pycall
end

macro std.types.to-bool
    "" "bool(stack.pop())"
    pycall
end

macro std.types.to-int
    "" "int(stack.pop())"
    pycall
end

macro std.types.to-float
    "" "float(stack.pop())"
    pycall
end