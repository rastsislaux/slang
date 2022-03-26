#! /bin/python3.10

import subprocess
from os import listdir
from os.path import isfile, join
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description=
                                     """
                                     tool to test slang
                                     """)
    parser.add_argument("command",
                        choices=["test", "renew"],
                        help="test - run tests, renew to renew answers")
    parser.add_argument("-t", "--test", help="test (all tests by default)",
                        type=str, default="")
    return parser.parse_args()


def run(test: str):
    command = ["src/pyslang.py", "run", f"tests/{test}.slang"]
    sub = subprocess.Popen(command, stdout=subprocess.PIPE)
    text, retcode = sub.stdout.read(), sub.wait()
    return text


def main():

    args = parse_args()
    to_test = []
    if args.test == "":
        to_test = [f[:-6] for f in listdir("tests") if isfile(join("tests", f)) and f.endswith(".slang")]
    else:
        to_test = [args.test]

    match args.command:

        case "test":
            for test in to_test:
                with open(f"tests/out/{test}.out", "rb") as test_out_f:
                    test_out = test_out_f.read()
                if run(test) == test_out:
                    print(f"[X] {test}")
                else:
                    print(f"[ ] {test}")

        case "renew":
            for test in to_test:
                print(f"Test: {test}\n\t - started")
                with open(f"tests/out/{test}.out", "wb") as test_out_f:
                    test_out_f.write(run(test))
                print(f"\t - renewed")


if __name__ == "__main__":
    main()
