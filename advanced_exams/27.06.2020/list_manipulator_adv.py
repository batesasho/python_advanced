from collections import deque


def list_manipulator(sequence: list, command_one: str, command_two: str, *args):
    seq = sequence
    if (command_one, command_two) == ("add", "beginning"):
        seq = deque(sequence)
        seq.extendleft(args[::-1])
        return list(seq)
    elif (command_one, command_two) == ("remove", "beginning"):
        if args:
            return seq[args[0]:]
        else:
            return seq[1:]
    elif (command_one, command_two) == ("remove", "end"):
        if args:
            return seq[:-args[0]]
        else:
            return seq[:-1]
    elif (command_one, command_two) == ("add", "end"):
        seq.extend(args)
        return seq

# match (command_one, command_two):
#     case "add", "beginning":
#         seq = deque(sequence)
#         seq.extendleft(args[::-1])
#         return list(seq)
#     case "add", "end":
#         seq.extend(args)
#         return seq
#     case "remove", "beginning":
#         if args:
#             return seq[args[0]:]
#         else:
#             return seq[1:]
#     case "remove", "end":
#         if args:
#             return seq[:-args[0]]
#         else:
#             return seq[:-1]
    return

print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
