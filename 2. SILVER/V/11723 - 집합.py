import sys
input = sys.stdin.readline

S = set()
for _ in range(int(input())):
    command = input().strip().split()
    header = command[0]
    if header == 'add':
        S.add(int(command[1]))
    elif header == 'remove':
        if int(command[1]) in S:
            S.remove(int(command[1]))
        else:
            continue
    elif header == 'check':
        if int(command[1]) in S:
            print(1)
        else:
            print(0)
    elif header == 'toggle':
        if int(command[1]) in S:
            S.remove(int(command[1]))
        else:
            S.add(int(command[1]))
    elif command[0] == 'all':
        S = set(i for i in range(1, 21))
    else:
        S.clear()