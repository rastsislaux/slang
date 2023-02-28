/*
    THIS FILE IS A PART OF SLANG STANDARD LIBRARY.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.
*/

include std.types

macro std.io.print
    "" "print(stack[-1], end='')"
    pycall
    drop
end

macro std.io.println
    "" "print(stack[-1])"
    pycall
    drop
end

macro std.io.pop    std.io.print!   drop    end
macro std.io.popln  std.io.println! drop    end

macro std.io.peek
    "" "print(stack)"
    pycall
    drop
end

macro std.io.input
    "" "input()" pycall
end

macro std.io.puts using std.types namespaces
    to-str!
    std.io.pop!
end

macro std.io.putb using std.types namespaces
    to-bool!
    std.io.pop!
end

macro std.io.puti using std.types namespaces
    to-int!
    std.io.pop!
end

macro std.io.putf using std.types namespaces
    to-float!
    std.io.pop!
end

macro std.io.putx using std.types namespaces
    to-str!
    "hex(" + ")" swap + "" swap pycall
    std.io.pop!
end

macro std.io.putc using std.types namespaces
    to-str!
    "chr(" + ")" swap + "" swap pycall
    std.io.pop!
end