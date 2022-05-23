number = input().split()
stack_seq = []
for x in range(len(number)):
    stack_seq.append(number.pop())
print(" ".join(stack_seq))

