from collections import deque

text = input()

string_text = deque()
for el in range(len(text)):
    if text[el] == "(":
        string_text.append(el)
    elif text[el] == ")":
        print(text[string_text.pop():el+1])

