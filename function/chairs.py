from itertools import combinations
string = input().split(", ")
num = int(input())
[print(", ".join(el)) for el in combinations(string,num)]


