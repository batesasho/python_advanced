import sys
from collections import deque
from io import StringIO

input_1 = """100
100
Mercedes
green
Mercedes
BMW
Skoda
green
END
"""
#sys.stdin = StringIO(input_1)


def green_light_interval() -> int:
    return int(input())


def free_window_interval() -> int:
    return int(input())


def cars_and_green_light_sign() -> deque:
    command = input()
    cars_green_light_queue = deque()
    while not command == "END":
        cars_green_light_queue.append(command)
        command = input()
    else:
        return cars_green_light_queue


def count_car_name_letters(cars_list: deque) -> deque:
    car_names_count = deque()
    for names in cars_list:
        if not names == "green":
            car_names_count.append(len(names))
    return car_names_count


traffic_light_green_timer = green_light_interval()
traffic_free_window_timer = free_window_interval()
list_with_cars_and_green_signs = cars_and_green_light_sign()
list_with_count_car_names = count_car_name_letters(list_with_cars_and_green_signs)

traffic_light_timer = traffic_light_green_timer
traffic_window_timer = traffic_free_window_timer

passed_cars_successfully = deque()
is_crash = False
while list_with_cars_and_green_signs:

    if list_with_cars_and_green_signs[0] == "green":
        traffic_light_timer = traffic_light_green_timer
        traffic_window_timer = traffic_free_window_timer
        list_with_cars_and_green_signs.popleft()
        continue
    else:
        if traffic_light_timer == 0:
            break
        if len(list_with_cars_and_green_signs[0]) <= traffic_light_timer:
            traffic_light_timer -= len(list_with_cars_and_green_signs[0])
        else:
            if len(list_with_cars_and_green_signs[0]) <= traffic_light_timer + traffic_window_timer:
                traffic_window_timer -= abs(len(list_with_cars_and_green_signs) - traffic_light_timer)
                traffic_light_timer = 0
            else:
                is_crash = True
                crashed_on_letter = (traffic_window_timer+traffic_light_timer)
                break
        passed_cars_successfully.append(list_with_cars_and_green_signs.popleft())

if not is_crash:
    print('Everyone is safe.')
    print(f'{len(passed_cars_successfully)} total cars passed the crossroads.')
else:
    crashed_car = list_with_cars_and_green_signs[0]
    letter_crashed = crashed_car[crashed_on_letter]
    print("A crash happened!")
    print(f'{crashed_car} was hit at {letter_crashed}.')