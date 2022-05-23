import collections


def numbers_searching(*args) -> list:
    complete_sequence = set(x for x in range(min(set(args)), max(set(args)) + 1))
    current_sequence = set(args)
    missing_digit = complete_sequence.difference(current_sequence)
    dublicates = collections.Counter(args)

    return [*[x for x in missing_digit],
            [key for key, value in sorted(dublicates.items(), key = lambda x: x[0]) if value > 1]]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
