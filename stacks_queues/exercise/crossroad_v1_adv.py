import sys
from collections import deque
from io import StringIO

input_1 = """3
0
BMW
BMW
green
green
END"""
#sys.stdin = StringIO(input_1)

green_light_duration = int(input())
free_window_duration = int(input())

command = input()
car_queues = deque()
while not command == 'END':
    car_queues.append(command)
    command = input()
passing_car = []
flashing_green = green_light_duration
is_crash = False
current_car_before_green = deque()
while car_queues:
    if not car_queues[0] == "green":
        current_car_before_green.append(car_queues.popleft())
    else:
        car_queues.popleft()
        while current_car_before_green:
            if flashing_green == 0:
                break
            car = current_car_before_green.popleft()
            if flashing_green >= len(car):
                passing_car.append(car)
                flashing_green -= len(car)
            elif flashing_green + free_window_duration >= len(car):
                passing_car.append(car)
                break
            else:
                is_crash = True
                character_hit = car[flashing_green+free_window_duration]
                crashed_car = car
                break
    flashing_green = green_light_duration
    if is_crash:
        break
if is_crash:
    print("A crash happened!")
    print(f'{crashed_car} was hit at {character_hit}.')
else:
    print(f'Everyone is safe.')
    print(f"{len(passing_car)} total cars passed the crossroads.")
