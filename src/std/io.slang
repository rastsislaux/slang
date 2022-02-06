/*
    THIS FILE IS A PART OF SLANG STANDARD LIBRARY.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2022
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.
*/

macro std.io.print
    "print(stack[-1], end='')"
    pycall
    drop
end

macro std.io.println
    "print(stack[-1])"
    pycall
    drop
end

macro std.io.pop    std.io.print!   drop    end
macro std.io.popln  std.io.println! drop    end

macro std.io.peek
    "print(stack)"
    pycall
    drop
end

macro std.io.input
    "input()" pycall
end