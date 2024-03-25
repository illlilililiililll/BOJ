a = int(input())
count = 0
num = list(map(int, input().split()))
def prime(n):
    m = []
    for i in range(1, n+1):
        if n % i == 0:
            m.append(i)
    if len(m) == 2:
        return True

for _ in range(a):
    if prime(num[_]) == True:
        count += 1

print(count)