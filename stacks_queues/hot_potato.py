from collections import deque

names = deque(input().split())
toss_number = int(input())


while len(names) > 1 :
    for _ in range(toss_number - 1):
        names.append(names.popleft())
    print(f'Removed {names.popleft()}')

else:
    print(f'Last is {names.pop()}')