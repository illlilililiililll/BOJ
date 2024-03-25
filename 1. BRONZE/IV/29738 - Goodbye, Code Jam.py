import sys
input = sys.stdin.readline

for _ in range(1, int(input())+1):
    rank = int(input())
    final = 0
    if rank > 4500:
        final = 1
    elif rank > 1000:
        final = 2
    elif rank > 25:
        final = 3
    else:
        final = 4
    if final != 4:
        print(f'Case #{_}: Round {final}')
    else:
        print(f'Case #{_}: World Finals')