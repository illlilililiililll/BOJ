import sys
from collections import Counter
input = sys.stdin.readline

extension = []
for _ in range(int(input())):
    extension.append(input().rstrip().split('.')[1])
count = sorted(Counter(extension).most_common(), key=lambda x:(x[0], x[1]))
for i in range(len(count)):
    print(count[i][0], count[i][1])