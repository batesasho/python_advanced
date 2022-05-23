def recursive_power(number: int, power: int) -> int:
    # x = 1
    # for i in range(power):
    #     x *= number
    # return x

    if power == 1:
        return number

    return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))
