def operate(operator: str, *args):

    if operator == "+":
        result = 0
        result = sum(args)
        return result
    elif operator == "-":
        result = args[0]
        for el in range(1,len(args)):
            result -= args[el]
        return result
    elif operator == "*":
        result = args[0]
        for el in range(1, len(args)):
            result *= args[el]
        return result
    elif operator == "/":
        result = args[0]
        for el in range(1, len(args)):
            result /= args[el]
        return result


print(operate("/", 6, 4))
