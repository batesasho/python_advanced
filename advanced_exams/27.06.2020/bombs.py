from collections import deque

input_1 = """30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10"""
# sys.stdin = StringIO(input_1)

bomb_effect = deque(list(map(int, input().split(", "))))
bomb_casing = deque(list(map(int, input().split(", "))))

materials = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120,
}
bombs_counting = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
count = 0
is_bomb_pouch = False
bomb = []
while bomb_effect and bomb_casing:
    mix_sum = bomb_effect[0] + bomb_casing[-1]
    if mix_sum in materials.values():
        name_material = [k for k, v in materials.items() if v == mix_sum][0]
        bombs_counting[name_material] += 1
        bomb.append(mix_sum), bomb_effect.popleft(), bomb_casing.pop()
    else:
        bomb_casing[-1] -= 5
    bomb_pouch = [(k, v) for k, v in bombs_counting.items() if v > 2]
    if len(bomb_pouch) > 2:
        is_bomb_pouch = True
        break

if is_bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effect:
    print("Bomb Effects: empty")
else:
    print(f'Bomb Effects: {", ".join(str(x) for x in bomb_effect)}')

if not bomb_casing:
    print("Bomb Casings: empty")
else:
    print(f'Bomb Casings: {", ".join(str(x) for x in bomb_casing)}')

print(*[f"{name}: {count}" for name, count in sorted(bombs_counting.items(), key = lambda x: x[0])], sep = "\n", )
