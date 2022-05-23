from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])
count_matches = 0
while males and females:
    if females[0] <= 0:
        females.popleft()
        continue
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    if males[-1] % 25 == 0:
        males.pop()
        males.pop()
        continue
    if females[0] == males[-1]:
        count_matches += 1
        females.popleft()
        males.pop()
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {count_matches}")
if not males:
    print("Males left: none")
else:
    print(f'Males left: {", ".join([str(males[x]) for x in range(-1, -len(males)-1,-1)])}')
if not females:
    print("Females left: none")
else:
    print(f'Females left: {", ".join(map(str, females))}')
