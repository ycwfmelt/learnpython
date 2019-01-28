from contextlib import contextmanager


@contextmanager
def context_illustration():
    print("entering context.")

    try:
        yield
    except Exception as e:
        print("leaving context.")
        print("with an error {}".format(e))

        raise
    else:
        print("leaving context.")
        print("with no error.")

if __name__ == '__main__':
    context_illustration()