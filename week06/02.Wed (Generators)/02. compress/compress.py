# Compress


def compress(iterable, mask):
    both = zip(iterable, mask)
    return [i for i, j in both if j is True]


def main():
    mask = list(compress(["Creed", "Michael", "Kevin"], [True, False, False]))
    print(mask)


if __name__ == '__main__':
    main()