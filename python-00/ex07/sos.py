import sys


def main():
    if (len(sys.argv) != 2):
        raise AssertionError("the arguments are bad")
    NESTED_MORSE = {
            ' ': '/ ',
            'A': '.- ',
            'B': '-... ',
            'C': '-.-. ',
            'D': '-.. ',
            'E': '. ',
            'F': '..-   . ',
            'G': '--. ',
            'H': '.... ',
            'I': '.. ',
            'J': '.--- ',
            'K': '-.- ',
            'L': '.-.. ',
            'M': '-- ',
            'N': '-. ',
            'O': '--- ',
            'P': '.--. ',
            'Q': '--.- ',
            'R': '.-. ',
            'S': '... ',
            'T': '- ',
            'U': '..- ',
            'V': '...- ',
            'W': '.-- ',
            'X': '-..- ',
            'Y': '-.-- ',
            'Z': '--.. ',
            '1': '.---- ',
            '2': '..--- ',
            '3': '...-- ',
            '4': '....- ',
            '5': '..... ',
            '6': '-.... ',
            '7': '--... ',
            '8': '---.. ',
            '9': '----. ',
            '0': '----- ',
        }
    input = sys.argv[1].upper()
    morse = ""
    for i in input:
        if i not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        morse += NESTED_MORSE[i]
    print(morse)


if __name__ == "__main__":
    main()
