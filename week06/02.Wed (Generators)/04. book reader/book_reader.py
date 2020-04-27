# Book Reader
import os


def book_reader(file):
    with open(file, 'r') as f:
        chapter = str()
        for line in f:
            if line[0] == '#':
                if chapter != '':
                    yield chapter
                chapter = str()

            chapter += line
        yield chapter


def increment_string_index(stringIndex):
    value = int(stringIndex)
    value += 1

    if value > 99:
        newStringIndex = str(value)

    elif value > 9:
        newStringIndex = "0" + str(value)

    elif value >= 0:
        newStringIndex = "00" + str(value)

    else:
        raise IndexError("Negative index!")

    return newStringIndex


def main():
    idx = "000"

    while True:
        idx = increment_string_index(idx)

        fname = f"Book/{idx}.txt"

        if not os.path.isfile(fname):
            break

        else:
            read = book_reader(fname)
            while True:
                try:
                    chapter = next(read)
                except StopIteration:
                    break

                print(chapter)

                while True:
                    space = input()
                    if space == ' ':
                        break

    print("You have reached the end!")


if __name__ == '__main__':
    main()
