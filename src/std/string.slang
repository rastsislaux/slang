macro std.string.split
    "" "stack.pop().split()" pycall
end

macro std.string.splitby
    "" "stack.pop().split(stack.pop())" pycall
end