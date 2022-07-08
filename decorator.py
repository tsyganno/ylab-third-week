def cash(func):
    dictionary = {}

    def inner(*args):
        if args not in dictionary:
            dictionary[args] = func(*args)
        return dictionary[args]
    return inner


@cash
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    print(multiplier(2))
    print(multiplier(4))
    print(multiplier(2))
