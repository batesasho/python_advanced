symbols = ['.', '?', '""', "'", ',', '-', '!', ':', ';', '...', '[', '[', '(', ')']

with open('text.txt', 'r') as file, open('result.txt', 'w') as result_file:
    content_lines = file.readlines()
    for num in range(len(content_lines)):
        count_letters = 0
        count_punctuation_marks = 0
        for letter in content_lines[num]:
            if letter.isalpha():
                count_letters += 1
            elif letter in symbols:
                count_punctuation_marks += 1
        line_print_file = content_lines[num][:-2]
        print(
            f'Line {num + 1}: {line_print_file} ({count_letters})({count_punctuation_marks})',file=result_file)
