from collections import deque


def math_operations(*args, **kwargs):
    seq_list = deque(args)
    math_operation_dict = kwargs
    i = 0
    while seq_list:
        if i == len(math_operation_dict):
            i = 0
        if i == 0:
            math_operation_dict['a'] += seq_list.popleft()
        elif i == 1:
            math_operation_dict['s'] -= seq_list.popleft()
        elif i == 2:
            if not seq_list[0] == 0:
                math_operation_dict['d'] /= seq_list.popleft()
            else:
                seq_list.popleft()
        elif i == 3:
            math_operation_dict['m'] *= seq_list.popleft()
        i += 1
    return math_operation_dict


print(math_operations(2, 12, 0, -3, 6, -20, -11, a = 1, s = 7, d = 33, m = 15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
