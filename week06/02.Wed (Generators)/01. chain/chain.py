# Chain


# Ok version
def chain1(iterable_one, iterable_two):
    concatenated = []

    for item in iterable_one:
        concatenated.append(item)

    for item in iterable_two:
        concatenated.append(item)

    return concatenated


# Better
def chain2(iterable_one, iterable_two):
    concatenated = []

    concatenated.extend(iterable_one)
    concatenated.extend(iterable_two)

    return concatenated


# GODLIKE
def chain3(iterable_one, iterable_two):
    return [*iterable_one, *iterable_two]


# Generator version
def chain_g(iterable_one, iterable_two):
    for item in iterable_one:
        yield item

    for item in iterable_two:
        yield item


def main():

    concatenation = list(chain1(range(0, 4), {"four": 4, 5: "five"}))
    print(concatenation)

    concatenation = list(chain2(range(0, 4), {"four": 4, 5: "five"}))
    print(concatenation)

    concatenation = list(chain3(range(0, 4), {"four": 4, 5: "five"}))
    print(concatenation)

    concatenation = list(chain_g(range(0, 4), {"four": 4, 5: "five"}))
    print(concatenation)


if __name__ == '__main__':
    main()