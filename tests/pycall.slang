/*

    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 06.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    This program prints all numbers from 1 to 15.

    It is also compiled to slang bytecode (print-numbers.sx),
    you can execute it by running:
        - pyslang run print-numbers.slang
        - pyslang exe print-numbers.sx

*/

macro main

    "this sys"              // first arg stands for needed libraries
    "print(sys.version)"    // the second is the statement to be evaluated
    pycall

end