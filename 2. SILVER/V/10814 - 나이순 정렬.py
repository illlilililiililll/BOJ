import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    age, name = input().split()
    age = int(age)
    data.append([age, name])

data.sort(key=lambda x: x[0])
for _ in range(n):
    print(data[_][0], data[_][1])