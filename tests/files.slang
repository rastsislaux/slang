/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    This program opens a file and prints it

*/

include std.io
include std.fs

const PATH_TO_FILE "./tests/etc/file-to-open.txt"

macro print-file-contents using std namespaces
    "r" PATH_TO_FILE! fs.file-open!
    dup     fs.reads!   io.popln!
    fs.file-close!
end

macro write-to-file using std namespaces
    PATH_TO_FILE! fs.file-open!
    dup "Lorem ipsum dolor sit amet.\n" swap fs.writes! drop
    fs.file-close!
end

macro main using std namespaces

    "File before editing:"  io.popln!
    print-file-contents!


    "a" write-to-file!
    "File after appending:" io.popln!
    print-file-contents!

    "w" write-to-file!
    "File after rewriting:" io.popln!
    print-file-contents!

end