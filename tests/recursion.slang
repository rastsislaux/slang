/* #include <iostream>

using namespace std;

string no_recursion(int number, int system) {
    string result = "";
    while (number >= system) {
        result = to_string(number % system) + result;
        number = number / system;
    }
    result = to_string(number) + result;
    return result;
}

string recursion(int number, int system) {
    if (number < system)
        return to_string(number);
    string result = recursion(number / system, system) + to_string(number % system);
    return result;
}

int main() {
    int n, p;
    cout << "Введите числа N и P (0<P<10): ";
    cin >> n >> p;
    cout << no_recursion(n, p) << " " << recursion(n, p);
}
 */

include std.io
include std.types

macro no-recursion using std.types namespaces
    $number swap &
    $system swap &

    $result "" &
    ($system @ $number @ >=) while
        $result dup @
        ($system @ $number @ %)to-str!
        + &
        $number dup @ $system @ swap / to-int! &
    ($system @ $number @ >=) do

    $result dup @
    ($number @)to-str! + &

    $result @
end

macro recursion using std.types namespaces
    $number swap &
    $system swap &

    ($system @ $number @ <) if
        ($number @)to-str! return
    fi

    $result "" &
    ($system @ $number @ %)to-str!

    (
        $system @,
        ($system @ $number @ /)to-int!
    )recursion!

    + return

end

macro main using std.io namespaces
    (2, 154)no-recursion!
    (2, 154)recursion!
    popln! popln!
end