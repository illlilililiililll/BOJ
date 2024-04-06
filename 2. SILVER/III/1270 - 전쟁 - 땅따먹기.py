import sys
import collections
input = sys.stdin.readline

for _ in range(int(input())):
    T = list(map(int, input().split()))
    n = T.pop(0)

    T = collections.Counter(T).most_common(1)[0]
    
    if T[1]/n > 0.5:
        print(T[0])
    else:
        print("SYJKGW")