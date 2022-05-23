from collections import deque
import sys

from io import StringIO

input_1 = """10, 5, 8, 9
2, 4, 5, 8"""

#sys.stdin = StringIO(input_1)
customers = deque(int(x) for x in input().split(", "))
taxis = deque(int(x) for x in input().split(", "))

total_time = 0
while customers and taxis:
    if taxis[-1] >= customers[0]:
        total_time += customers[0]
        taxis.pop()
        customers.popleft()
    else:
        taxis.pop()

if not taxis and not customers:
    print("All customers were driven to their destinations", f"\nTotal time: {total_time} minutes")
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(map(str,customers))}")


