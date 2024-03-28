import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

num = deque()
for _ in range(n):
    num.append(input().strip())

count = 0
while True:
    new = set([i[-(count+1):] for i in num])
    count += 1
    # print(new)
    if len(new) == len(num):
        break
    # print(new, count)

print(count)