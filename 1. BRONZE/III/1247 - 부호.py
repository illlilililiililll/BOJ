import sys
input = sys.stdin.readline
for _ in range(3):
    sum = 0
    for _ in range(int(input())):
        sum += int(input())
    if sum == 0:
        print(0)
    elif sum > 0:
        print('+')
    else:
        print('-')