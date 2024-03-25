import sys
from collections import Counter
input = sys.stdin.readline

num = []
for _ in range(int(input())):
    num.append(int(input()))

count = sorted(Counter(num).most_common(), key=lambda x: (-x[1], x[0]))
print(count[0][0])