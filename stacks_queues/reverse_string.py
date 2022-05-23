from collections import deque

text = deque("I Love Python")
while text:
    print(text.pop(),end="")