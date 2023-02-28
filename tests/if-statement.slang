/*
    THIS FILE IS A PART OF SLANG EXAMPLES.
    AUTHOR: Rostislav Lipsky (https://github.com/ungaf)
    DATE: 26.02.2023
    VISIT https://github.com/ungaf/slang AND READ THE LICENSE BEFORE USING.

    This is an example of using nested if statements.
*/

include std.io

macro main using std.io namespaces

    // If-else flow
    0 5 <
    dup if "5 is less than 0"    popln! fi
    not if "5 is greater than 0" popln! fi

    // Nested if statement
    true if
        "first layer"  popln!
        "first layer2" popln!
        False if
            "second layer"  popln!
            "second layer2" popln!
            True if
                "third layer"  popln!
                "third layer2" popln!
            fi
        fi
        "first layer3" popln!
    fi

    // slang doesn't have else keywords, instead of it use:
    false dup // some condition
    if
        "This is not printed." popln!
    fi
    not if
        "This is printed." popln!
    fi


end