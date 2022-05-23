def even_odd(*args):
    *args, command = args

    if command == "odd":
        return [x for x in args if not x % 2 == 0]
    return [x for x in args if x % 2 == 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
