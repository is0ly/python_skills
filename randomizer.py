import random

word = 'Moscow'
print(random.choice(word))


def random_list_generator(minimum, maximum, length):
    result = []
    while length != 0:
        result.append(random.randint(minimum, maximum))
        length -= 1
    return result


print(random_list_generator(10, 100, 20))
