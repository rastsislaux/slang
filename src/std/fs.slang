/*
    THIS FILE IS A PART OF SLANG STANDARD LIBRARY.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 08.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.
*/

macro std.fs.file-open
    "" "open(stack.pop(), stack.pop())" pycall
end

macro std.fs.file-close
    "" "stack.pop().close()" pycall drop
end

macro std.fs.reads
    "" "stack.pop().read()" pycall
end

macro std.fs.writes
    "" "stack.pop().write(stack.pop())" pycall
end