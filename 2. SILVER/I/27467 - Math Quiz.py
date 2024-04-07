import sys
import collections
input = sys.stdin.readline

N = input()
num = [i%3 for i in list(map(int, input().split()))]

count = sorted(collections.Counter(num).most_common(), key=lambda x: x[0])
p = 0
q = 0

for n, m in count:
    if n == 0:
        q += m
    elif n == 1:
        p += m
    elif n == 2:
        p -= m
        q -= m

print(float(p), float(q))