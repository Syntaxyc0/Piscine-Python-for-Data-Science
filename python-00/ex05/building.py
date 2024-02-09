

import sys
import string


def main():
    """
    Program which takes a single string argument
    and displays the sums of its upper-case characters,
    lower-case characters, punctuation characters, digits and spaces.
    """
    argc = len(sys.argv)
    if argc > 2:
        raise AssertionError("Too many arguments")
    if argc == 1:
        try:
            arg = input("What is the text to count?\n")
        except EOFError:
            return
    else:
        arg = sys.argv[1]
    print("the text contains", len(arg), "characters:")
    print(sum(1 for c in arg if c.isupper()), "upper letters")
    print(sum(1 for c in arg if c.islower()), "lower letters")
    print(sum(1 for c in arg if c in string.punctuation), "punctuation marks")
    print(sum(1 for c in arg if c.isspace()), "spaces")
    print(sum(1 for c in arg if c.isdigit()), "digits")


if __name__ == '__main__':
    main()
