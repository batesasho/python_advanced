import sys
from collections import deque
from io import StringIO

input_1 = """50
2
11 10 5 11 10 20
15 13 16
1500"""

sys.stdin = StringIO(input_1)


def price_of_each_bullet() -> int:
    return int(input())


def size_of_gun_barrel() -> int:
    return int(input())


def bullets_sequence() -> deque:
    return deque(map(int, input().split()))


def locks_sequence() -> deque:
    return deque(map(int, input().split()))


def value_of_intelligence() -> int:
    return int(input())


price_of_bullet_deque = price_of_each_bullet()
size_of_gun_barrel_deque = size_of_gun_barrel()
bullets_sequence_deque = bullets_sequence()
locks_sequence_deque = locks_sequence()
intelligence_deque = value_of_intelligence()
bullets_shooted_counter = 0

is_safe_unlock = False
test = deque()
while locks_sequence_deque:
    if not bullets_sequence_deque:
        is_safe_unlock = True
        break
    if len(locks_sequence_deque) % size_of_gun_barrel_deque == 0 \
        and bullets_shooted_counter:
        print("Reloading!")
    bullets_shooted_counter += 1
    if bullets_sequence_deque[-1] <= locks_sequence_deque[0]:
        bullets_sequence_deque.pop()
        locks_sequence_deque.popleft()
        print("Bang!")
    else:
        bullets_sequence_deque.pop()
        print("Ping!")

else:
    money_earned = intelligence_deque - bullets_shooted_counter * price_of_bullet_deque
    print(f"{len(bullets_sequence_deque)} bullets left. Earned ${money_earned}")

if is_safe_unlock:
    print(f"Couldn't get through. Locks left: {len(locks_sequence_deque)}")
