/* Slang (shitty language) is a language written just for fun.
   First I've thought to create a real interpretator but
   that was too hard for me so I've created a translator. 
   
   MIT, Rostislav Lipsky 2021 */

/* You can import Python libraries: */

pyinclude os;

pyinclude slang_stdlib *;

/* You can include Slang modules: */

include method;

/*  This is a usual function.
    Parameters are stored after keyword with.
    Return type is stored after keyword returns. */

function write_and_return with integer a returns integer;

    write a;

    return a;

end;

function return2 with nothing returns integer; return 2; end;

/*  This is the main function.
    Keyword nothing after with means that it has no parameters.
    nothing after returns means that this function doesn't return anything. */

function main with nothing returns nothing;

    /* Slang is a strong-typed language. Actually, sometimes
       you can not declare variables but this will lead to
       undefined behaviour. */

    string strn;
    double dbl;
    integer intg;
    boolean bln;
    vector vect;

    /* There are some built-in procedures, such as:
        - write
        - append (old version of list.append)
        - set
        Other functions are derived from python. */

    write "Hello," _SPC "world!" _NWL;

    /* Vectors in slang can contain variables of different types.
       There's to ways to append elements to vector.
       Method append from slang.stdlib and pythonic list.append */

    append vect 123;
    vect.append "TESTING";

    /* write method can print any types */

    write vect _NWL;

    /* set is a method of assignment */

    set strn "hello!";
    set dbl 12.5;
    set intg 13;
    set bln True;

    /* Previously custom and Python methods required a variable
       to return into. Now it doesn't */

    return2;
    return2 -> intg;

    print "Hello!";
    print "Hello!" -> strn;

    /* Slang supports while statements, for is not implemented.
       There should be no spaces in condition. */

    while intg<26;

        write intg _SPC;
        inc intg 2 -> intg;

    end;

    /* Use break to end the cycle. */

    while True;
        
        write intg _SPC;
        inc intg -> intg;

        /*  It was supposed to work like that:
        boolean condition;
        equals intg 50 -> condition;
        if condition; break; end;
            But it also works this way: */
        
        if intg==51; break; end;

    end;

    write _NWL;

    /* Instead of for there is python-like foreach: */

    vector numbers;
    set numbers [1,2,3,4,5,6,7,8,9,10];

    range 0 10 2 -> rng;
    foreach i in rng;

        write numbers[i] _SPC;
    
    end;

    write _NWL;

    /* Dictionaries implementation: */

    dict dictionary;
    dictionary.update {"key":"value","key2":"value2"};

    write dictionary["key"] _NWL;

end;
