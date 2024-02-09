import sys

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("AssertionError: more than one argument is provided")
        return 1
    try:
        integer = int(args[0])
    except:
        print("AssertionError: argument is not an integer")
        return 1
    if (integer % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
        

if __name__ == '__main__':
    main()