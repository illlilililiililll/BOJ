import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
num = deque([i for i in range(1, n+1)])
while len(num) > 1:
    num.popleft()
    num.append(num.popleft())

print(num[0])