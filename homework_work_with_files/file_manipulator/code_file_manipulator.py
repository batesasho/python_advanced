import os
import sys
from io import StringIO

input_1 = """Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
Delete-file.txt
End"""
sys.stdin = StringIO(input_1)

command = input()

while not command == "End":
    command = command.split("-")
    if command[0] == "Create":
        with open(command[1], "w") as file:
            pass
    elif command[0] == "Add":
        with open(command[1], "a+") as file:
            file.write(command[2]+"\n")

    elif command[0] == "Replace":
        try:
            with open(command[1], 'r+') as file:
                content = file.readlines()
                content = "".join([el.replace(command[2], command[3]) for el in content])
            with open(command[1], 'wt') as file:
                file.write(content)
        except:
            print("An error occurred")
    elif command[0] == "Delete":
        if os.path.exists(command[1]):
            os.remove(command[1])
        else:
            print("An error occurred")
    command = input()
