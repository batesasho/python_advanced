import sys
from collections import deque
from io import StringIO

input_1 = """ROB-1;SS2-5;NX8000-6
8:00:00
detail
glass
wood
apple
piano
fire
steel
silver
gold
metal
basket
trash
End"""


sys.stdin = StringIO(input_1)


def robot_information() -> [dict, list, list]:
    """receive from the console the robot information - name, processing_time -> create a dictionary"""
    command = input().split(";")
    robot_info = {}
    for elements in command:
        name, processing_time = elements.split("-")
        robot_info.setdefault(name, int(processing_time))
    return robot_info, [x for x in robot_info.values()], [x for x in robot_info.keys()]


def starting_time() -> int:
    """converting time in seconds"""
    time = input().split(":")
    return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])


def convert(seconds) -> str:
    """converting time in hh:mm:ss"""
    seconds %= 24 * 3600
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hour:02d}:{minutes:02d}:{seconds:02d}"


def input_details() -> deque:
    """receive from the console the detail's information - different details are placed into a deque"""
    command = input()
    details = deque()
    while not command == "End":
        details.append(command)
        command = input()
    else:
        return details


(
    robot_details_dictionary,
    robot_processing_time_list,
    robot_names,
) = robot_information()  # names : processing time
initial_time = starting_time() + 1
deque_details_for_processing = input_details()
temporary_list = robot_processing_time_list.copy()
i = 0
while deque_details_for_processing:

    if i == len(robot_processing_time_list):
        i = 0
    if temporary_list[i] == robot_processing_time_list[i]:
        print(f"{robot_names[i]} - {deque_details_for_processing[0]} [{convert(initial_time)}]")
        deque_details_for_processing.popleft()
        temporary_list[i] = 0

    else:
        deque_details_for_processing.append(deque_details_for_processing.popleft())
    temporary_list = [temporary_list[x] + 1 if temporary_list[x] < robot_processing_time_list[x] else temporary_list[x]
                      for x in range(len(temporary_list))]
    initial_time += 1
    i += 1

