import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())
    l = set()
    for _ in range(m):
        l.add(int(input()))

    if len(l) == 1:
        print(1)
    else:
        i = 2
        while True:
            new = set([j%i for j in l])
            if len(new) == len(l):
                print(i)
                break
            i += 1