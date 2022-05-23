def sequence_of_numbers() -> list:
    return list(map(int, input().split()))


def separate_negative_positive(seq: list) -> tuple:
    positive_numbers = [x for x in seq if x >= 0]
    negative_number = [x for x in seq if x < 0]
    return sum(positive_numbers), sum(negative_number)


def print_result(positive: list, negative: list) -> print:
    print(negative)
    print(positive)

    if abs(negative) > abs(positive):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")

sequence = sequence_of_numbers()
positive, negative = separate_negative_positive(sequence)
print_result(positive, negative)