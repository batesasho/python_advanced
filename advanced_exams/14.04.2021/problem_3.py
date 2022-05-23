def flights(*args):
    destination = [args[x] for x in range(len(args)) if x % 2 == 0]
    passenger = [args[x] for x in range(len(args)) if not x % 2 == 0]
    flight_information = {}
    for index in range(len(destination)):
        if destination[index] == "Finish":
            break
        flight_information.setdefault(destination[index], 0)
        flight_information[destination[index]] += passenger[index]

    return flight_information


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
