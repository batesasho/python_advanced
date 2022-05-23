import sys
from collections import deque
from io import StringIO

input_1 = """5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22"""

#sys.stdin = StringIO(input_1)

fireworks_effect = deque(map(int, input().split(", ")))
explosive_power = deque(map(int, input().split(", ")))

palm_firework = []
willow_firework = []
crossette_firework = []
is_successfull = False
while fireworks_effect and explosive_power:
    if fireworks_effect[0] <= 0:
        fireworks_effect.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue
    if (fireworks_effect[0] + explosive_power[-1]) % 3 == 0 and not (fireworks_effect[0] + explosive_power[
        -1]) % 5 == 0:
        palm_firework.append(fireworks_effect.popleft() + explosive_power.pop())
    elif (fireworks_effect[0] + explosive_power[-1]) % 5 == 0 and not (fireworks_effect[0] + explosive_power[
        -1]) % 3 == 0:
        willow_firework.append(fireworks_effect.popleft() + explosive_power.pop())
    elif (fireworks_effect[0] + explosive_power[-1]) % 5 == 0 and (fireworks_effect[0] + explosive_power[-1]) % 3 == 0:
        crossette_firework.append(fireworks_effect.popleft() + explosive_power.pop())
    else:
        fireworks_effect[0] -= 1
        fireworks_effect.append(fireworks_effect.popleft())

    if len(palm_firework) >= 3 and len(willow_firework) >= 3 and len(crossette_firework) >= 3:
        is_successfull = True
        break

if is_successfull:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effect:
    print(f'Firework Effects left: {", ".join(map(str,fireworks_effect))}')
if explosive_power:
    print(f'Explosive Power left: {", ".join(map(str,explosive_power))}')

print(f"Palm Fireworks: {len(palm_firework)}")
print(f"Willow Fireworks: {len(willow_firework)}")
print(f"Crossette Fireworks: {len(crossette_firework)}")

