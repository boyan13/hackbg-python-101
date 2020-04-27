# Performance (file name)
from time import time, sleep


def performance(filename):
    def wrap(func):
        def inner(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            total = time() - start
            with open(filename, 'a') as f:
                f.write("{} was called and took {} seconds to complete\n".format(
                    func.__name__, int(total)))
            return result
        return inner
    return wrap


@performance("log.txt")
def main():
    sleep(2)


if __name__ == '__main__':
    main()
