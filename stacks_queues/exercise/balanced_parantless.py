from collections import deque

text = deque(input())
new_dq = deque()

if len(text) % 2 == 0:

    for index_elements in range(len(text)):

        if text[0] == '{' or text[0] == '[' or text[0] == '(':
            new_dq.append(text.popleft())

        else:
            if (text[0] != ')' or new_dq[-1] != '(') and (text[0] != '}' or new_dq[-1] != '{') and (
                    text[0] != ']' or new_dq[-1] != '['):
                print("NO")
                break
            else:
                text.popleft()
                new_dq.pop()

    else:
        if new_dq == text:
            print('YES')
        else:
            print("NO")
else:
    print("NO")
