def sort_pair(args):
    x, y = args
    if x > y:
        return y, x
    return x, y


print(sort_pair((5, 1)))
print(sort_pair((5, 4)))
print(sort_pair((5, 14)))
