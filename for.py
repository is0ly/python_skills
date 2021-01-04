animals = ['lion', 'cat', 'monkey', 'horse', 'behemoth', 'python']
animals_weight = {
    'lion': 400,
    'cat': 8,
    'monkey': 12,
    'horse': 350,
    'behemoth': 900,
    'python': 70
}

letters_count = 0


def lines():
    print('\n*************************************************')
    print('*************************************************')
    print('*************************************************\n')


for animal in animals:
    print('Now ----> ', animal)
    letters_count += len(animal)

print('All letters is: ', letters_count)

lines()


for i, animal in enumerate(animals):
    print(i, animal)

lines()


for i in range(30, 51, 5):
    print(i)


lines()


def get_animal_weight(zoo):
    all_weight = 0
    for weight in zoo:
        all_weight += zoo[weight]
    return all_weight


print(get_animal_weight(animals_weight))