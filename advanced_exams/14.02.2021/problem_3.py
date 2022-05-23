def stock_availability(inventory_list: list, delivery_or_sell, *args):
    if delivery_or_sell == "delivery":
        inventory_list.extend(args)
    elif delivery_or_sell == "sell":
        if not args:
            inventory_list = inventory_list[1:]
        elif isinstance(args[0], int):
            inventory_list = inventory_list[args[0]:]
        else:
            inventory_list = [x for x in inventory_list if x not in args]
    return inventory_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
