def input_text():
    return input()


def count_symbols(input_sequence: str):
    sequence_dictionary = {}
    for elements in input_sequence:
        sequence_dictionary.setdefault(elements, 0)
        sequence_dictionary[elements] += 1
    return sequence_dictionary


def printing_sequence_dictionary_ordered(sequence_dict: dict):
    [print(f'{letter}: {count} time/s') for letter, count in sorted(sequence_dict.items(), key = lambda x: x[0])]


sequence_entered = input_text()
count_entered_symbols = count_symbols(sequence_entered)
printing_sequence_dictionary_ordered(count_entered_symbols)


