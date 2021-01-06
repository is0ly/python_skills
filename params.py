def print_them_all_v1(*args):
    print(type(args))
    print(args)
    for i, arg in enumerate(args):
        if type(arg) == list:
            print(arg)
        print('Позиционный параметр: ', i, arg)


def print_them_all_v2(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print("Позиционный параметр", key, "=", value)


print_them_all_v1(1, 2, 'Hello', [1, 2, 'Cat'])

print_them_all_v2(name='Ivan', city="Moscow")
