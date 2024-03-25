import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    num = set(map(int, input().split()))
    m = int(input())
    find = list(map(int, input().split()))
    for i in find:
        print(1 if i in num else 0)