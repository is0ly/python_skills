# TODO

def summation(nums):  # normal function
    return sum(nums)


def main(f, *args):  # function as an argument
    result = f(*args)
    print(result)


if __name__ == "__main__":
    main(summation, [1, 2, 3, 5])  # output 6


