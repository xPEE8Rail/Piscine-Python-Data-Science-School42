import sys


def process(sym, num):
    # constants
    ASCII_MIN = 0
    ASCII_MAX = 127
    UP_MIN_LETTER = 65  # A
    UP_MAX_LETTER = 90  # Z
    LOW_MIN_LETTER = 97  # a
    LOW_MAX_LETTER = 122  # z
    SIZE = 26

    sym = ord(sym)
    if sym < ASCII_MIN or sym > ASCII_MAX:
        raise ValueError('The script does not support your language yet')
    if UP_MIN_LETTER <= sym <= UP_MAX_LETTER:
        sym += num
        if sym > UP_MAX_LETTER:
            sym = UP_MIN_LETTER + (sym - UP_MAX_LETTER - 1) % SIZE
        elif sym < UP_MIN_LETTER:
            sym = UP_MAX_LETTER - (UP_MIN_LETTER - sym - 1) % SIZE
    elif LOW_MIN_LETTER <= sym <= LOW_MAX_LETTER:
        sym += num
        if sym > LOW_MAX_LETTER:
            sym = LOW_MIN_LETTER + (sym - LOW_MAX_LETTER - 1) % SIZE
        elif sym < LOW_MIN_LETTER:
            sym = LOW_MAX_LETTER - (LOW_MIN_LETTER - sym - 1) % SIZE
    return chr(sym)


def encode(text, num):
    new_s = ""
    for i in text:
        new_s += process(i, num)
    return new_s


def decode(text, num):
    new_s = ""
    for i in text:
        new_s += process(i, -num)
    return new_s


def cipher(rule, text, num):
    if rule == "encode":
        return encode(text, num)
    elif rule == "decode":
        return decode(text, num)
    raise ValueError("The string is not correct!")


def main():
    if len(sys.argv) == 4:
        try:
            result = cipher(sys.argv[1], sys.argv[2], int(sys.argv[3]))
            print(result)
        except ValueError:
            print("Number parameter is not correct!")

    else:
        raise RuntimeError("Invalid number of arguments")


if __name__ == "__main__":
    main()
