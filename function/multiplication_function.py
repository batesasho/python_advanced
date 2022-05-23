def multiply(*args):
    multiple=1
    for x in args:
        multiple *= x
    return multiple

x = multiply(1,2,3,4)

print(x)