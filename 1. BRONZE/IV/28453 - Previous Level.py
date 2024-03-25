n = int(input())

level = list(map(int, input().split()))

for _ in range(n):
    lv = level[_]
    if lv == 300:
        print('1', end=' ')
    elif lv >= 275:
        print('2', end=' ')
    elif lv >= 250:
        print('3', end=' ')
    else:
        print('4', end=' ')