# @accepts decorator


def accepts(*types):
    def wrap(func):
        def inner(*args):
            z = zip(args, types)
            for arg, argtype in z:
                # IsInstance comparison (e.g. 12 is an instance of int)
                if not isinstance(arg, argtype):
                    raise TypeError("Argument \'{}\' of \'{}\' is not {}".format(
                        arg, func.__name__, argtype.__name__))
        return inner
    return wrap
