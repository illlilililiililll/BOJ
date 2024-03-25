import sys
from collections import Counter
input = sys.stdin.readline

n = input()
arr = Counter(map(int, input().split()))
m = input()
for i in list(map(int, input().split())):
    count = arr[i]
    print(count, end=' ')