import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]

print(round(sum(num)/n))
num.sort()
print(num[(n-1)//2])
count = Counter(num).most_common()
if len(count) == 1:
    print(count[0][0])
elif count[0][1] == count[1][1]:
    print(count[1][0])
else:
    print(count[0][0])
print(max(num)-min(num))