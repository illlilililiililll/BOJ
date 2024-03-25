import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
num = deque([i for i in range(1, n+1)])
result = []

while len(num) > 0:
    num.rotate(-m+1)
    result.append(str(num.popleft()))

print('<'+', '.join(result)+'>')