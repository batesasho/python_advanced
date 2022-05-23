from collections import deque

pizza_orders = deque(map(int, input().split(", ")))
employees_pizza_capacity = deque(map(int, input().split(", ")))

count = 0

while pizza_orders and employees_pizza_capacity:
    if pizza_orders[0] <= 0 or pizza_orders[0] > 10:
        pizza_orders.popleft()
        continue
    if pizza_orders[0] <= employees_pizza_capacity[-1]:
        count += pizza_orders.popleft()
        employees_pizza_capacity.pop()
    else:
        pizza_orders[0] -= employees_pizza_capacity[-1]
        count += employees_pizza_capacity.pop()
if not pizza_orders:
    print("All orders are successfully completed!")
    print(f'Total pizzas made: {count}')
    print(f'Employees: {", ".join(map(str, employees_pizza_capacity))}')
else:
    print("Not all orders are completed.")
    print(f'Orders left: {", ".join(map(str, pizza_orders))}')
