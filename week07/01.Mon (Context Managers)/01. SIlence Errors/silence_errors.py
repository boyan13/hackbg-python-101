# Silence Errors
from contextlib import contextmanager


class silence_exception():

    def __init__(self, exc, message=None):
        silence_exception.validate(exc, message)
        self.exc = exc
        self.message = message

    @staticmethod
    def validate(exc, message):
        if type(exc) is not type:
            raise TypeError("Expected an exception type.")
        elif Exception not in exc.mro():
            raise TypeError("Expected an exception type.")
        if message is not None and type(message) is not str:
            raise TypeError("Expected string.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if isinstance(exc_value, self.exc):
            if self.message is None:
                return True
            else:
                return (str(exc_value) == self.message)


@contextmanager
def func_silence_exception(exc, message=None):

    def validate(exc, message):
        if type(exc) is not type:
            raise TypeError("Expected an exception type.")
        elif Exception not in exc.mro():
            raise TypeError("Expected an exception type.")
        if message is not None and type(message) is not str:
            raise TypeError("Expected string.")

    validate(exc, message)

    try:
        yield
    except Exception as exception:
        if isinstance(exception, exc):
            if message is None:
                return True
            else:
                return (str(exception) == message)


def main():
    with func_silence_exception(ValueError, "gayzer"):
        raise ValueError("Test")


if __name__ == '__main__':
    main()