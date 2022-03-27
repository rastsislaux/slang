macro std.list.new
    "" "[]" pycall
end

macro std.list.append
    "" "stack.pop().append(stack.pop())" pycall drop
end

macro std.list.clear
    "" "stack.pop().clear()" pycall drop
end

macro std.list.copy
    "" "stack.pop().copy()" pycall
end

macro std.list.count
    "" "stack.pop().count()" pycall
end

macro std.list.size
    "" "len(stack.pop())" pycall
end

macro std.list.index
    "" "stack.pop().index(stack.pop())" pycall
end

macro std.list.contains
    "" "stack.pop().__contains__(stack.pop())" pycall
end

macro std.list.pop
    "" "stack.pop().pop()" pycall
end

macro std.list.ipop
    "" "stack.pop().pop(stack.pop())" pycall
end

macro std.list.get
    "" "stack.pop()[stack.pop()]" pycall
end

macro std.list.set
    "" "stack.pop().__setitem(stack.pop(), stack.pop())" pycall
end

macro std.list.insert
    // {object} {index} {list} std.list.insert!
    "" "stack.pop().insert(stack.pop(), stack.pop())" pycall drop
end

macro std.list.reverse
    "" "stack.pop().reverse()" pycall drop
end

macro std.list.sort
    "" "stack.pop().sort()" pycall drop
end

macro std.list.unpack using std.list namespaces
    $array swap &
    $size ($array @)size! &

    ($size @ 0 !=) while
        ($array @)pop!
        $size dup @ -- &
    ($size @ 0 !=) do
end