from datetime import datetime


def cache_decorate(func):
    cache = {}

    def wrapper(arg):
        if arg not in cache:
            cache[arg] = func(arg)
        return cache[arg]

    return wrapper


@cache_decorate
def factorial(n):
    if n == 1:
        return 1;
    return factorial(n - 1) * n


def factorial2(n):
    if n == 1:
        return 1;
    return factorial2(n - 1) * n


start = datetime.now()
factorial(200)
print("Time laps: ", (datetime.now() - start).microseconds)

start2 = datetime.now()
factorial2(200)
print("Time laps: ", (datetime.now() - start2).microseconds)

