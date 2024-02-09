import sys
import string
from ft_filter import ft_filter


def main():
    """
    program that accepts two arguments: a string(S), and an integer(N). The
    program outputs a list of words from S that have a length greater than N.
    """
    if (len(sys.argv) != 3):
        raise AssertionError("the arguments are bad")
    try:
        len_min = int(sys.argv[2])
    except Exception:
        raise AssertionError("the arguments are bad")
    input = sys.argv[1]
    for i in input:
        if i in string.punctuation or not i.isprintable():
            raise AssertionError("the arguments are bad")
    split_input = input.split(" ")
    print(list(ft_filter(lambda x: len(x) > len_min, split_input)))


if __name__ == "__main__":
    main()
