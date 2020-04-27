# Cycle


def cycle(iterable):
    i = iterable

    while True:
        for item in i:
            yield item

        i = iterable


def main():
    endless = cycle(range(0, 10))
    for item in endless:
        print(item)


if __name__ == '__main__':
    main()