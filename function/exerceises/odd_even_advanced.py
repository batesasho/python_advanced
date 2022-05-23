def print_result(seq: list, command: str) -> print:
    if command == "Odd":
        odd = sum(x for x in seq if not x % 2 == 0)
        print(odd*len(seq))
    else:
        print(sum(x for x in seq if x % 2 == 0)*len(seq))


command = input()
sequence = list(map(int,input().split()))
print_result(sequence, command)
