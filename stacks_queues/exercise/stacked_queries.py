number = int(input())

stack = []
for num in range(number):
    command = input().split()
    try:
        if command[0] == "1":
            stack.append(int(command[1]))
        elif command[0] == '2':

            stack.pop()
        elif command[0] == '3':

            print(max(stack))
        elif command[0] == '4':

            print(min(stack))
    except:

        pass
else:
    print(*stack[::-1], sep = ", ")
