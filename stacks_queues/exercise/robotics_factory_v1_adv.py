from collections import deque

input_1 = """ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End"""


# sys.stdin = StringIO(input_1)


def robots_info() -> tuple:
    """add robots information - names and processing time period """
    robots_name, robots_processing_time, common_list = [], [], {}
    robots = input().split(";")
    for robot in robots:
        name, time = robot.split("-")
        robots_name.append(name)
        robots_processing_time.append(int(time))
        common_list.setdefault(name, int(time))

    return robots_name, robots_processing_time


def starting_time() -> int:
    """converting hh:mm:ss in seconds"""
    time = input().split(":")
    return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])


def convert(seconds) -> tuple:
    """converting seconds in hh:mm:ss"""
    seconds %= 24 * 3600
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return hour, minutes, seconds


def products_sequence() -> list:
    """A list with all the details for processing"""
    command = input()
    product_list = []
    while not command == "End":
        product_list.append(command)
        command = input()
    return product_list


robots_name, robots_processing_time = robots_info()
start_working_time_in_seconds = starting_time()
products_list = deque(products_sequence())
processing_time = robots_processing_time.copy()

while products_list:
    start_working_time_in_seconds += 1
    detail = products_list.popleft()
    hour, minutes, seconds = convert(start_working_time_in_seconds)

    for robot_time in robots_processing_time:
        if start_working_time_in_seconds >= robot_time:
            robot_name_printing = robots_name[robots_processing_time.index(robot_time)]
            print(f'{robot_name_printing} - {detail} [{hour:02d}:{minutes:02d}:{seconds:02d}]')
            robots_processing_time[robots_processing_time.index(robot_time)] = \
                start_working_time_in_seconds + processing_time[robots_processing_time.index(robot_time)]
            break
    else:
        products_list.append(detail)
