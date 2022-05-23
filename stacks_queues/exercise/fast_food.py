from collections import deque

food_quantity = int(input())
order_quantity = deque(map(int, input().split()))

print(max(order_quantity))

while order_quantity:
    if food_quantity >= order_quantity[0]:
        food_quantity -= order_quantity.popleft()
    else:
        break

if not order_quantity:
    print('Orders complete')
else:
    print(f'Orders left: {" ".join([str(x) for x in order_quantity])}')
