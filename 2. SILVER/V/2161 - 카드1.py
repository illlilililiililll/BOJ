import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stack = deque([str(i) for i in range(1, n+1)])
result = []

while len(stack) >= 2:
    result.append(stack.popleft())
    stack.append(stack.popleft())

result.append(stack[0])
print(' '.join(result))