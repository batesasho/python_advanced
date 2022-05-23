from collections import deque


def fill_the_box(height, length, width, *args):
    size_of_box = height * length * width
    qubes_list = deque(args)

    while not qubes_list[0] == "Finish":
        if size_of_box <= 0 :
            break
        if size_of_box >= qubes_list[0]:
            size_of_box -= qubes_list.popleft()
        else:
            qubes_list[0] -= size_of_box
            size_of_box = 0
    else:
         return f'There is free space in the box. You could put {size_of_box} more cubes.'
    return f"No more free space! You have {sum([x for x in qubes_list if isinstance(x, int)])} more cubes."



print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
