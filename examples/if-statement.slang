/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 26.02.2022
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    This is an example of using nested if statements.
*/

from /home/rostislove/Git/slang/src/
    include std.io

macro main using std.io namespaces

    // If-else flow
    0 5 <
    dup if "5 is less than 0"    popln! fi
    not if "5 is greater than 0" popln! fi

    // Nested if statement
    true if
        "first layer"  println!
        "first layer2" println!
        False if
            "second layer"  println!
            "second layer2" println!
            True if
                "third layer"  println!
                "third layer2" println!
            fi
        fi
        "first layer3" println!
    fi

end