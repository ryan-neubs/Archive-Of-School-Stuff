# tests.py


"""
    runs all example files and tells you which ones pass and which ones fail
"""

import os
import checker as chk


def main():

    for fname in os.listdir('./examples'):
        if fname.endswith(".jle"):
            with open("./examples/" + fname) as f:
                chars = f.read()
            f.close()
            try:
                check = chk.JelleChecker(chars)
                check.check_program()
                print("File", fname, "ran successfully")
            except SyntaxError as e:
                print("------------ UNEXPECTED ERROR ---------------")
                print("syntax error in file", fname)
                print("Error:", e)
    for fname in os.listdir("./examples/error"):
        if fname.endswith("jle"):
            with open("./examples/error/" + fname) as f:
                chars = f.read()
            f.close()
            try:
                check = chk.JelleChecker(chars)
                check.check_program()
                print("---------ERROR DIDN'T FAIL-----------")
                print("File:", fname, "expected an error")
            except SyntaxError:
                print("File:", fname, "failed successfully")

                

if __name__ == "__main__":
    main()
