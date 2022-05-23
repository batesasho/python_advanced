from collections import deque

q_calc = deque()
for el in range(int(input())):
    petrol, distance = input().split()
    q_calc.append(int(petrol)-int(distance))

tank, el, starting_station = 0, 0, 0

while el < len(q_calc):
    if q_calc[0] < 0 or tank < 0:
        q_calc.append(q_calc.popleft())
        el, tank = 0, 0
        starting_station += 1
        continue
    else:
        tank += q_calc[el]
    el += 1
else:
    print(starting_station)

