from collections import deque

clothes = deque(map(int,input().split()))
capacity = int(input())

current_sum = 0
count = 0
new = []
while True:
    try:
        if capacity >= current_sum + clothes[-1]:
             current_sum += clothes.pop()
        else:
            new.append(current_sum)
            current_sum = 0
            count += 1
    except: # terminate if end of queue
        count += 1
        break

print(count)







